#!/usr/bin/env python3

import cairo
import math

def DrawTransition(surface, x1, x2, y1, y2, colour, width, label, fs):
	ctx = cairo.Context(surface)
	arrow_length = abs(y1 - y2) - width
	arrow_angle = math.pi / 2
	arrowhead_angle = math.pi/6
	arrowhead_length = width * 1.5

	ctx.move_to(x1, y1) # move to center of canvas

	ctx.rel_line_to(arrow_length * math.cos(arrow_angle), arrow_length * math.sin(arrow_angle))
	ctx.rel_move_to(-arrowhead_length * math.cos(arrow_angle - arrowhead_angle), -arrowhead_length * math.sin(arrow_angle - arrowhead_angle))
	ctx.rel_line_to(arrowhead_length * math.cos(arrow_angle - arrowhead_angle), arrowhead_length * math.sin(arrow_angle - arrowhead_angle))
	ctx.rel_line_to(-arrowhead_length * math.cos(arrow_angle + arrowhead_angle), -arrowhead_length * math.sin(arrow_angle + arrowhead_angle))
	ctx.set_line_width(width)

	ctx.set_source_rgb(colour[0], colour[1], colour[2])
	ctx.set_line_width(width)
	ctx.stroke()

	ctx.move_to(x1 + 0.5 * width, y1 - 0.5 * width) # move to center of canvas

	ctx.set_source_rgb(colour[0], colour[1], colour[2])
	ctx.select_font_face("Times",
	        cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
	ctx.set_font_size(fs)

	ctx.save()

	ctx.rotate( - math.pi / 4)
	ctx.show_text(label)
	ctx.restore()
	
	return ctx

def DrawLevel(surface, Energy, x1, x2, colour, width, label, fs, pos):
	ctx = cairo.Context(surface)
	arrow_length = abs(x1 - x2)


	# Text stuff
	ctx.set_source_rgb(colour[0], colour[1], colour[2])
	ctx.select_font_face("Times",
	        cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
	ctx.set_font_size(fs)
	x_off, y_off, tw, th = ctx.text_extents(label)[:4]

	if pos == "l":
		arrow_length = arrow_length - tw

	# Draw Level
	ctx.move_to(x1, Energy) # move to center of canvas

	ctx.rel_line_to(arrow_length, 0)

	ctx.set_source_rgb(colour[0], colour[1], colour[2])
	ctx.set_line_width(width)
	ctx.stroke()

	# Draw text
	if pos == "b":
		ctx.move_to(x2 - tw, Energy + width + th) # move to center of canvas	
	elif pos == "l":
		#Do nothing! 
		pass
	else:
		ctx.move_to(x2 - tw, Energy - width) # move to center of canvas

	ctx.show_text(label)

	return ctx


# =======================================================================

class Branch:
  def __init__(self, offset):
    self.Offset = offset 
    self.b_levels = []
    self.b_transitions = []
  def AddLevel(self, level):
    self.b_levels.append(level)
  def AddTransition(self, transition):
    self.b_transitions.append(transition)

class Level:
  branches = []
  Position = "a"
  def __init__(self, Energy, Colour, Width):
    self.Energy = Energy
    self.Colour = Colour
    self.Width = Width
    self.Label = str(Energy) + " keV"

  def AddBranch(self, branch):
    self.branches.append(branch)

#  def Func(self):
#	print("Hello my name is " + self.Energy)

class Transition:
  def __init__(self, Start, End, Colour, Width, Label):
    self.Start     = Start    
    self.End       = End      
    self.Colour    = Colour   
    self.Width     = Width    
    self.Label     = Label

class Scheme:
  Transitions = []
  Levels = []
  FontSize = 12
  TitleFont = 24

  def __init__(self, WIDTH, PIXEL_SCALE, TITLE):
    self.PIXEL_SCALE = PIXEL_SCALE
    self.WIDTH  = WIDTH
    self.TITLE = TITLE
    self.BranchNo  = 1

  def SetFontSize(self, FontSize):
    self.FontSize = FontSize

  def SetTitleFontSize(self, TitleFont):
    self.TitleFont = TitleFont

  def AddLevel(self, lvl):
    self.Levels.append(lvl)
    self.BranchNo = self.BranchNo + len(lvl.branches)

  def AddTransition(self, gamma):
    self.Transitions.append(gamma)

  def Draw(self, Filename):
    HEIGHT = 0

    if self.BranchNo != 0:
      for L in self.Levels:
        for B in L.branches:
          for BL in B.b_levels:
            if BL.Energy > HEIGHT:
              HEIGHT = BL.Energy

    if HEIGHT == 0:
      for L in self.Levels:
        if L.Energy > HEIGHT:
          HEIGHT = L.Energy

 
    x  = 0.2 * self.WIDTH
    if(len(self.Transitions) != 0):
        dx = 0.6 * self.WIDTH / (len(self.Transitions) * self.BranchNo)
    else:
        dx = 0.1 * self.WIDTH
    HEIGHT = int(HEIGHT * 1.2)

    surface = cairo.ImageSurface(cairo.FORMAT_RGB24,
                             self.WIDTH*self.PIXEL_SCALE,
                             HEIGHT*self.PIXEL_SCALE)
    ctx = cairo.Context(surface)
    ctx.scale(self.PIXEL_SCALE, self.PIXEL_SCALE)	

    ctx.rectangle(0, 0, self.WIDTH, HEIGHT)
    ctx.set_source_rgb(1, 1, 1)
    ctx.fill()

    HEIGHT = HEIGHT - (HEIGHT * 0.1 / 1.2)

	#=========== DRAW LEVELS ============
    for L in self.Levels:
        b_count = 1 
        if len(self.Transitions) <= 1:
            b_count = 0
        ctx = DrawLevel(surface, HEIGHT - L.Energy, 0.1 * self.WIDTH, self.WIDTH - 0.1 * self.WIDTH, L.Colour, L.Width, L.Label, self.FontSize, L.Position)
        if(self.BranchNo != 0):
            for B in L.branches:
                bx = 0.1 * self.WIDTH + b_count * (0.8 * self.WIDTH / self.BranchNo) + (0.8 * 0.1 * self.WIDTH / self.BranchNo) 
                dx2 = (0.8 * 0.8 * self.WIDTH / self.BranchNo) / len(B.b_transitions)
                for BL in B.b_levels:
                    ctx = DrawLevel(surface, HEIGHT - BL.Energy, 0.1 * self.WIDTH + b_count * (0.8 * self.WIDTH / self.BranchNo),
                                             self.WIDTH - 0.1 * self.WIDTH - (self.BranchNo - b_count - 1) * (0.8 * self.WIDTH / self.BranchNo),
                                             BL.Colour, BL.Width, BL.Label, self.FontSize, BL.Position)
                bx = bx - B.Offset
                for BT in B.b_transitions:
                    ctx = DrawTransition(surface, bx, bx, HEIGHT - BT.Start, HEIGHT - BT.End, BT.Colour, BT.Width, BT.Label, self.FontSize)
                    bx = bx + dx2
                b_count = b_count + 1

	#=========== DRAW TRANSITIONS ============
    for T in self.Transitions:
        ctx = DrawTransition(surface, x, x, HEIGHT - T.Start, HEIGHT - T.End, T.Colour, T.Width, T.Label, self.FontSize)
        x = x + dx


	#=========== DRAW GRAPH ============

    ctx.set_source_rgb(0,0,0)
    ctx.select_font_face("Times",
            cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(self.TitleFont)
    
    x_off, y_off, tw, th = ctx.text_extents(self.TITLE)[:4]
    ctx.move_to(0.5 * self.WIDTH - 0.5 * tw, HEIGHT + 1.5 * th) # move to center of canvas
    ctx.show_text(self.TITLE)

    surface.write_to_png(Filename)










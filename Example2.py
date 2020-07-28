
#from DrawLevels import Scheme, Level, Transition
import DrawLevels as DL


# Set up level scheme ================================
# Scheme( GraphWidth , PixelDensity , NucleiName) 
bing = DL.Scheme(1800, 1, "60Ni")
bing.SetFontSize(60)
bing.SetTitleFontSize(80)

# If only branches - no main levels
bing.BranchNo = 0

# Add Ground Level ===================================
L3 = DL.Level(0, [0,0,0], 10)

# Add branch =========================================
# Branch( OffsetXPos ) 
B0 = DL.Branch( 0 )


# Add levels and transitions to branch ===============
L1 = DL.Level((1173 + 1332), [0,0,0], 10)
B0.AddLevel(L1)
L2 = DL.Level(1332, [0,0,0], 10)
B0.AddLevel(L2)

T1 = DL.Transition((1173+1332), 1332, [0,0,1], 15, "1173 keV")
B0.AddTransition(T1)
T2 = DL.Transition(1332, 0, [1,0,0], 15, "1332 keV")
B0.AddTransition(T2)

# Add Branch to ground level =========================
L3.AddBranch(B0)

# Add branch =========================================
# Branch( OffsetXPos ) 
B1 = DL.Branch( 40 )


# Add levels and transitions to branch ===============
L4 = DL.Level(1000, [0,0,0], 10)
B1.AddLevel(L4)
L5 = DL.Level(1184, [0,0,0], 10)
B1.AddLevel(L5)
L6 = DL.Level(785, [0,0,0], 10)
B1.AddLevel(L6)

T4 = DL.Transition(1184, 0, [0,1,0], 15, "1184 keV")
B1.AddTransition(T4)
T5 = DL.Transition(1000, 785, [0,1,0], 15, "215 keV")
B1.AddTransition(T5)
T5 = DL.Transition(785, 0, [0,1,0], 20, "785 keV")
B1.AddTransition(T5)

# ===================================================


# Add Branch to ground level =========================
L3.AddBranch(B1)
bing.AddLevel(L3) # and level to the scheme (after adding branch)

# Draw Picture =======================================
bing.Draw("ExampleLevelScheme_2.png")



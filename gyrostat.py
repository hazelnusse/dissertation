from sympy import symbols, simplify, latex
from sympy.physics.mechanics import (inertia, inertia_of_point_mass, mprint,
        mlatex, Point, ReferenceFrame)

Ixx, Iyy, Izz, Ixz, I, J = symbols("I_xx I_yy I_zz I_xz I J")
mA, mB, lx, lz = symbols("m_A m_B l_x l_z")

A = ReferenceFrame("A")
IA_AO = inertia(A, Ixx, Iyy, Izz, 0, 0, Ixz)
IB_BO = inertia(A, I, J, I)

BO = Point('BO')
AO = BO.locatenew('AO', lx*A.x + lz*A.z)
CO = BO.locatenew('CO', mA / (mA + mB) * AO.pos_from(BO))
print(mlatex(CO.pos_from(BO)))

IC_CO = IA_AO + IB_BO +\
        inertia_of_point_mass(mA, AO.pos_from(CO), A) +\
        inertia_of_point_mass(mB, BO.pos_from(CO), A)

mprint((A.x & IC_CO & A.x).expand())
mprint((A.y & IC_CO & A.y).expand())
mprint((A.z & IC_CO & A.z).expand())
mprint((A.x & IC_CO & A.z).expand())


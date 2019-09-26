from sympy import *
T, U, Q = symbols('T U Q')
a, b, c, d, u, l = symbols('a b c d u l')

# Equations for internal energy of the thermal mass of the third floor
Q_Sun_E_u = 0 #TODO: Write expression for Q_Sun_E_u
Q_Sun_S_u = 0 #TODO: Write expression for Q_Sun_S_u
Q_U_a = 0 #TODO: Write expression for Q_U_a
Q_U_b = 0 #TODO: Write expression for Q_U_b
Q_U_c = 0 #TODO: Write expression for Q_U_c
Q_U_d = 0 #TODO: Write expression for Q_U_d
dU_u_dt = Q_Sun_E_u + Q_Sun_S_u - Q_U_a - Q_U_b - Q_U_c - Q_U_d

# Equations for internal energy of the thermal mass of the second floor
Q_Sun_E_l = 0 #TODO: Write expression for Q_Sun_E_l
Q_Sun_S_l = 0 #TODO: Write expression for Q_Sun_S_l
Q_L_c = 0 #TODO: Write expression for Q_L_c
Q_L_d = 0 #TODO: Write expression for Q_L_d
dU_l_dt = Q_Sun_E_l + Q_Sun_S_l - Q_L_c - Q_L_d

# Equations for internal energy of the air in section A (third floor south endcap)
Q_b_a = 0 #TODO: Write expression for Q_b_a
Q_a_out = 0 #TODO: Write expression for Q_a_out
dU_a_dt = Q_U_a + Q_b_a - Q_a_out

# Equations for internal energy of the air in section B (third floor middle section)
Q_b_out = 0 #TODO: Write expression for Q_b_out
dU_b_dt = Q_U_b - Q_b_a - Q_b_out

# Equations for internal energy of the air in section C (second floor south endcap)
Q_d_c = 0 #TODO: Write expression for Q_d_c
Q_c_out = 0 #TODO: Write expression for Q_c_out
dU_c_dt = Q_U_c + Q_L_c + Q_d_c - Q_c_out

# Equations for internal energy of the air in section D (second floor middle section)
Q_d_out = 0 #TODO: Write expression for Q_d_out
dU_d_dt = Q_U_d + Q_L_d - Q_d_c - Q_d_out

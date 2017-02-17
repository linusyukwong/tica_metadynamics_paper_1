plumed_script="RESTART \n\
TORSION ATOMS=5,7,9,15 LABEL=phi_0_1 \n\
TORSION ATOMS=7,9,15,17 LABEL=psi_1_2 \n\
MATHEVAL ARG=phi_0_1 FUNC=sin(x)--0.815241623066 LABEL=sin_phi_0_1 PERIODIC=NO \n\
MATHEVAL ARG=phi_0_1 FUNC=cos(x)--0.131125790906 LABEL=cos_phi_0_1 PERIODIC=NO \n\
MATHEVAL ARG=psi_1_2 FUNC=sin(x)-0.286726096227 LABEL=sin_psi_1_2 PERIODIC=NO \n\
MATHEVAL ARG=psi_1_2 FUNC=cos(x)--0.314836222992 LABEL=cos_psi_1_2 PERIODIC=NO \n\
COMBINE LABEL=tic_0 ARG=sin_phi_0_1,cos_phi_0_1,sin_psi_1_2,cos_psi_1_2 COEFFICIENTS=3.78464062942,0.984827650367,0.239609635308,0.21932004493 PERIODIC=NO \n\
METAD ARG=tic_0 SIGMA=0.1 HEIGHT=0.2 FILE=HILLS PACE=1000 LABEL=metad \n\
PRINT ARG=tic_0,metad.bias STRIDE=1000 FILE=COLVAR \n"
print(plumed_script)

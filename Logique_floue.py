import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

error = ctrl.Antecedent(np.arange(-4, 5, 1), 'error')
error_dot = ctrl.Antecedent(np.arange(-10, 11, 1), 'error_dot')
percent = ctrl.Consequent(np.arange(-100, 101, 1), 'percent')

error['TH'] = fuzz.trapmf(error.universe, [-4, -4, -2, 0])
error['JR'] = fuzz.trimf(error.universe, [-2, 0, 2])
error['TC'] = fuzz.trapmf(error.universe, [0, 2, 4, 4])
error.view()

error_dot['GH'] = fuzz.trapmf(error_dot.universe, [-10, -10, -5, 0])
error_dot['NC'] = fuzz.trimf(error_dot.universe, [-5, 0, 5])
error_dot['GC'] = fuzz.trapmf(error_dot.universe, [0, 5, 10, 10])
error_dot.view()

percent['C'] = fuzz.trapmf(percent.universe, [-100, -100, -50, 0])
percent['DN'] = fuzz.trimf(percent.universe, [-50, 0, 50])
percent['H'] = fuzz.trapmf(percent.universe, [0, 50, 100, 100])
percent.view()

rule1 = ctrl.Rule(error['TC'] & error_dot['GC'], percent['H'])
rule2 = ctrl.Rule(error['TC'] & error_dot['NC'], percent['H'])
rule3 = ctrl.Rule(error['TC'] & error_dot['GH'], percent['H'])
rule4 = ctrl.Rule(error['JR'] & error_dot['GC'], percent['H'])
rule5 = ctrl.Rule(error['JR'] & error_dot['NC'], percent['DN'])
rule6 = ctrl.Rule(error['JR'] & error_dot['GH'], percent['C'])
rule7 = ctrl.Rule(error['TH'] & error_dot['GC'], percent['C'])
rule8 = ctrl.Rule(error['TH'] & error_dot['NC'], percent['C'])
rule9 = ctrl.Rule(error['TH'] & error_dot['GC'], percent['C'])

rules = []
for i in range(1, 10):
    rules.append(eval("rule" + str(i)))

#plante sans raison, c'est le fun
percent_ctrl = ctrl.ControlSystem(rules)
percent_ctrl.view()

percent_ctrl_sil = ctrl.ControlSystemSimulation(percent_ctrl)


percent_ctrl_sil.input['error'] = -1.5
percent_ctrl_sil.input['error_dot'] = -4
percent_ctrl_sil.compute()
print(percent_ctrl_sil.output['percent'])
percent.view(sim=percent_ctrl_sil)

percent_ctrl_sil.input['error'] = 0.5
percent_ctrl_sil.input['error_dot'] = 1
percent_ctrl_sil.compute()
print(percent_ctrl_sil.output['percent'])
percent.view(sim=percent_ctrl_sil)

percent_ctrl_sil.input['error'] = -1.5
percent_ctrl_sil.input['error_dot'] = -1
percent_ctrl_sil.compute()
print(percent_ctrl_sil.output['percent'])
percent.view(sim=percent_ctrl_sil)

percent_ctrl_sil.input['error'] = 0.5
percent_ctrl_sil.input['error_dot'] = 4
percent_ctrl_sil.compute()
print(percent_ctrl_sil.output['percent'])
percent.view(sim=percent_ctrl_sil)

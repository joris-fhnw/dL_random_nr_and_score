from pytm import AbstractExercise
from pytm import Latex
from pytm import Output
from src.idealGasValues.cp_values import *
import random

class Exercise(AbstractExercise):
    T1_vek = [400, 450, 500, 550]
    T2_vek = [650, 700, 750, 800]
    T1 = 0
    T2 = 0
    counter = 0

    def start(self, Q12: float = None) -> Output:
        if Exercise.counter == 0:
            Exercise.T1 = random.choice(Exercise.T1_vek)
            Exercise.T2 = random.choice(Exercise.T2_vek)
            Exercise.counter += 1

        print(Exercise.T2)
        return self.output \
            .add_paragraph(Latex(f'''
            Luft wird bei konstantem Druck von einem Bar von {Exercise.T1} K auf {Exercise.T2} K erwärmt. Erstellen
            Sie die Energiebilanz und  berechnen Sie die dazu nötige spezifische Wärmemenge in kJ/kg.
            ''')) \
            .add_number_field(name='Q12',
                              label=Latex(r'Tragen Sie hier die berechnete Wärmemenge, in kJ/kg ein.'),
                              value=Q12) \
            .add_action('Loesung', self.loesung)\
            .add_action("Hint",self.hint)


    def loesung(self, Q12: str) -> Output:
        cp_av = (Cp_ave_Air(Exercise.T1)+Cp_ave_Air(Exercise.T2))/2  # [kJ/(kg K)]
        dh = h_ave_Air(Exercise.T2)-h_ave_Air(Exercise.T2)  # [kJ/kg] gibt selbes Resultat wie cp*dT
        Q12_ans = cp_av*(Exercise.T2-Exercise.T1)  # [kJ]
        score = 0
        if abs(Q12-Q12_ans) <= 5:
            answ = "Die spezifische Wärme wurde richtig berechnet!!\n"
            score += 2
        else:
            answ = f"Die spezifische Wärme wurde falsch berechnet, die richtige Lösung ist: {round(Q12_ans)} kJ/kg"


        return self.output \
            .add_paragraph(Latex(f'''
            {answ}.
            ''')) \
            .add_action('Back to start', self.start, Q12=Q12)

    def hint(self,Q12: str) -> Output:
        return self.output \
            .add_paragraph(Latex(f'''
            - Luft kann als ideales Gas betrachtet werden.\n
            - Bei konstanem Druck, kann die Enthalpie eines idealen Gases über ide Cp-Werte berechnet werden.\n
            - Die Cp Werte können Sie mithilfe des Anhangs A7.3 bestimmen.
            ''')) \
            .add_action('Back to start', self.start,Q12=Q12)
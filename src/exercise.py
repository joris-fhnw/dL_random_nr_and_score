from pytm import AbstractExercise
from pytm import Latex
from pytm import Output
from src.idealGasValues.cp_values import *
import random

T1_vek = [400, 450, 500, 550]
T2_vek = [650, 700, 750, 800]

T1 = 0
T2 = 0
counter = 0

class Exercise(AbstractExercise):


    def start(self, Q12: float = None,counter: float = counter, T1:float = None, T2:float = None) -> Output:
        if counter == 0:
            T1 = random.choice(T1_vek)
            T2 = random.choice(T2_vek)
            counter += 1
            print(T1)
        return self.output \
            .add_paragraph(Latex(f'''
            Luft wird bei konstantem Druck von einem Bar von {T1} K auf {T2} K erwärmt. Erstellen
            Sie die Energiebilanz und  berechnen Sie die dazu nötige spezifische Wärmemenge in kJ/kg.
            ''')) \
            .add_number_field(name='Q12',
                              label=Latex(r'Tragen Sie hier die berechnete Wärmemenge, in kJ/kg ein.'),
                              value=Q12) \
            .add_action('Loesung', self.loesung(T1,T2))\
            .add_action("Hint",self.hint)


    def loesung(self, Q12: str,T1:float,T2:float) -> Output:
        cp_av = (Cp_ave_Air(T1)+Cp_ave_Air(T2))/2  # [kJ/(kg K)]
        dh = h_ave_Air(T2)-h_ave_Air(T2)  # [kJ/kg] gibt selbes Resultat wie cp*dT
        Q12_ans = cp_av*(T2-T1)  # [kJ]
        score = 0
        if abs(Q12-Q12_ans) <= 5:
            answ = "Die spezifische Wärme wurde richtig berechnet!!\n"
            score += .1
        else:
            answ = f"Die spezifische Wärme wurde falsch berechnet, die richtige Lösung ist: {round(Q12_ans)} kJ/kg"


        return self.output \
            .add_paragraph(Latex(f'''
            {answ}.
            ''')) \
            .add_score(score)\
            .add_action('Back to start', self.start, Q12=Q12)

    def hint(self,Q12: str) -> Output:
        return self.output \
            .add_paragraph(Latex(f'''
            - Luft kann als ideales Gas betrachtet werden.\n
            - Bei konstanem Druck, kann die Enthalpie eines idealen Gases über ide Cp-Werte berechnet werden.\n
            - Die Cp Werte können Sie mithilfe des Anhangs A7.3 bestimmen.
            ''')) \
            .add_action('Back to start', self.start,Q12=Q12)
from experta import *


class Desease(Fact):
    """Info about deseases"""
    pass


class RobotCrossStreet(KnowledgeEngine):
    @Rule(Desease(AS.Desease << Desease(('garganta_inflamada') | ('dificuldade_de_respirar'))))
    def green_light(self):
        print("Diagnóstico de covid")


engine = RobotCrossStreet()
engine.reset()
engine.declare(
    Desease(input()))
engine.run()
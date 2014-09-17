# -*- coding: utf-8 -*-
from lettuce import *
import app.match as m


@step(u'Given: "([^"]*)" and "([^"]*)" start a match to "([^"]*)" sets')
def given_group1_and_group2_start_a_match_to_group3_sets(
        step,
        group1,
        group2,
        group3):
    world.match = m.Match(group1, group2, group3)


@step(u'Then: I see score: "([^"]*)"')
def then_i_see_score_group1(step, score):
    assert world.match.score_set() == score, \
        "Got %s" % world.match.score_set()


@step(u'When: "([^"]*)" won the "([^"]*)" set "([^"]*)"-"([^"]*)"')
def when_group1_won_the_group2_set_group3_group4(step, jugador,
                                                 nset, punto1,
                                                 punto2):
    world.match.ganoSet(jugador)
    world.match.guardarPuntuacion(punto1,
                               punto2,
                               nset,
                               jugador)


@step(u'And: "([^"]*)" won the "([^"]*)" set "([^"]*)"-"([^"]*)"')
def and_group1_won_the_group2_set_group3_group4(step, jugador,
                                                nset, punto1,
                                                punto2):
    world.match.ganoSet(jugador)
    world.match.guardarPuntuacion(punto1,
                               punto2,
                               nset,
                               jugador)


@step(u'Then: The match score is: "([^"]*)"')
def then_the_match_score_is_group1(step, score):
    # print (world.match.score_set())
    assert world.match.score_set() == score, \
        "Got %s" % world.match.score_set()

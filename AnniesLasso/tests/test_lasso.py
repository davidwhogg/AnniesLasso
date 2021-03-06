#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Unit tests for the lasso model class and associated functions.
"""

import numpy as np
import unittest
from AnniesLasso import lasso, utils


class TestLassoCannonModel(unittest.TestCase):

    def setUp(self):
        # Initialise some faux data and labels.
        labels = "ABCDE"
        N_labels = len(labels)
        N_stars = np.random.randint(1, 500)
        N_pixels = np.random.randint(1, 10000)
        shape = (N_stars, N_pixels)

        self.valid_training_labels = np.rec.array(
            np.random.uniform(size=(N_stars, N_labels)),
            dtype=[(label, '<f8') for label in labels])

        self.valid_fluxes = np.random.uniform(size=shape)
        self.valid_flux_uncertainties = np.random.uniform(size=shape)

    def get_model(self):
        return lasso.LassoCannonModel(
            self.valid_training_labels, self.valid_fluxes,
            self.valid_flux_uncertainties)

    def test_init(self):
        self.assertIsNotNone(self.get_model())

    def test_remind_myself_to_write_unit_tests_for_these_functions(self):
        m = self.get_model()
        m.label_vector = "A + B + C"
        self.assertIsNotNone(m.label_vector)

        with self.assertRaises(NotImplementedError):
            m.train()

        m._trained = True
        with self.assertRaises(NotImplementedError):
            m.predict(None)

        with self.assertRaises(NotImplementedError):
            m.fit([], [])
    
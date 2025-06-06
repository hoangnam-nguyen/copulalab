"""
This module implements Copula-based Statistical Arbitrage tools.
"""

from copulalab.copula_calculation import (
    find_marginal_cdf, sic, aic, hqic, construct_ecdf_lin, scad_penalty,
    scad_derivative, adjust_weights, to_quantile, fit_copula_to_empirical_data)
from copulalab import archimedean
from copulalab import elliptical
from copulalab import mixed_copulas
from copulalab.vine_copula_partner_selection import PartnerSelection
from copulalab.vinecop_generate import (RVineCop, CVineCop)
from copulalab.vinecop_strategy import CVineCopStrat

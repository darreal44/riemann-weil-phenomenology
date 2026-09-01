# Wrap the two pre-campaign stdlib scripts so pytest runs them too.
import os, runpy

HERE = os.path.dirname(os.path.abspath(__file__))


def test_cert_mu11_script():
    runpy.run_path(os.path.join(HERE, 'test_cert_mu11.py'), run_name='__not_main__')


def test_theta_endpoints_script():
    runpy.run_path(os.path.join(HERE, 'test_theta_endpoints.py'), run_name='__not_main__')

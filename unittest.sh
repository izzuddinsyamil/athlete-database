#!/bin/bash
echo "=============== Running unit testing using coverage ==============="
echo
coverage run --source='.' --omit='./venv/*, */migrations/*' manage.py test
echo
echo
echo "====================== Code coverage report ======================"
echo
coverage report -m
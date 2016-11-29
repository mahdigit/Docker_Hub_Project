# -*- coding: utf8 -*-

def Docker_test_cases(number):
    return Docker_test_cases_no[number]

Docker_test_cases_no = [
    # [number, description]
    ['0', "Docker Hub - Automated Test Cases"],
    ['1', "Docker_TC 01: Verify successful login to Docker Hub"],
    ['2', "Docker_TC 02: Verify user can't sign in to Docker Hub using wrong login details"],
    ['3', "Docker_TC 03: Verify New user can sign up to Docker Hub"],
    ['4', "Docker_TC 04: Verify user able to search on Docker Hub"],
    ['5', "Docker_TC 05: Verify existing user can reset password on Docker Hub"],
]

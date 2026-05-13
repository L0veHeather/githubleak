#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Synthetic project file for GSIL/GitHub leak detection testing.
Do not use these values in production systems.
"""

PROJECT_NAME = "github-leak-detection-test"

USER_PROFILE = {
    "ucid": "29365524",
    "role_phone": "18912816336",
    "environment": "github_leak_test",
}

SERVICE_CONFIG = {
    "service_name": "test-github-leak-service",
    "base_url": "https://test-github-leak.test.ke.com/api",
    "api-key": "sk-githubtestleak123",
}

DATABASE_CONFIG = {
    "username": "github_leak_test_user",
    "password": "TestGithubleak",
    "host": "db.test-github-leak.test.ke.com",
    "port": 3306,
}


def build_auth_header() -> dict:
    return {
        "X-UCID": USER_PROFILE["ucid"],
        "Authorization": f"Bearer {SERVICE_CONFIG['api-key']}",
    }


def main() -> None:
    print(f"project={PROJECT_NAME}")
    print(f"ucid={USER_PROFILE['ucid']}")
    print(f"db_user={DATABASE_CONFIG['username']}")


if __name__ == "__main__":
    main()

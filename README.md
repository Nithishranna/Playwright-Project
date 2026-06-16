# Playwright Automation Framework with CI/CD

## Overview

A cloud-ready Playwright Automation Framework built using Python and Pytest following the Page Object Model (POM) design pattern.

The framework supports:

* Playwright UI Automation
* Pytest Test Execution
* Page Object Model (POM)
* Data-Driven Testing using JSON
* Screenshot Capture on Failure
* HTML Reporting
* GitHub Actions CI/CD
* Docker Containerization
* Jenkins Pipeline Integration

---

## Tech Stack

* Python
* Playwright
* Pytest
* Git
* GitHub Actions
* Docker
* Jenkins
* JSON

---

## Project Structure

```text
Playwright-Project/
│
├── pages/
├── tests/
├── utils/
├── config/
├── test_data/
├── reports/
├── screenshots/
│
├── conftest.py
├── pytest.ini
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
└── README.md
```

---

## Automated Test Scenarios

### Login Test

* Open SauceDemo
* Login with valid credentials
* Verify successful navigation

### Add To Cart Test

* Login
* Add Sauce Labs Backpack
* Open Cart
* Verify Product

### Checkout Test

* Login
* Add Product
* Checkout
* Complete Order
* Verify Successful Purchase

---

## Running Tests

```bash
pytest -v
```

---

## Running Docker

Build Image:

```bash
docker build -t playwright-framework .
```

Run Container:

```bash
docker run playwright-framework
```

Using Docker Compose:

```bash
docker-compose up
```

---

## GitHub Actions CI/CD

Pipeline automatically executes:

* On Push
* On Pull Request

Workflow:

```text
Code Push
↓
GitHub Actions Triggered
↓
Dependencies Installed
↓
Playwright Tests Executed
↓
Results Generated
```

---

## Features Implemented

* Page Object Model
* Data-Driven Testing
* Reusable Fixtures
* Screenshot Capture on Failure
* HTML Reports
* GitHub Actions CI/CD
* Docker Support
* Jenkins Support

---

## Future Enhancements

* API Automation
* Parallel Execution
* Cross-Browser Execution
* AWS Deployment
* Allure Reporting
* Database Validation

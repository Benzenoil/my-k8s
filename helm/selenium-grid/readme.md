# Selenium grid on Kubernetes for Mac OS M1

This folder contains the necessary files for setting up Selenium Grid on a Kubernetes cluster on Mac OS.

## install

```bash
kubectl config current-context
# return docker-desktop 

helm repo add docker-selenium https://www.selenium.dev/docker-selenium

helm repo update

kubectl create ns selenium-grid

helm install selenium-grid docker-selenium/selenium-grid -n selenium-grid -f values.yaml
```

## simple test

```bash
python test/test_firefox.py
```
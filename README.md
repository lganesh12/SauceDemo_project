# SauceDemo_project

To run test cases behave --define browser=chromium --define headless=false --tags=@TC_01,@TC_02 features/

behave -f allure_behave.formatter:AllureFormatter -o allure-results ./features

behave -f allure_behave.formatter:AllureFormatter -o allure-results ./features --tags=TC_01,~not_implemented

docker run --rm -it -e HEADLESS=false behave-tests

docker run --rm -it behave-tests

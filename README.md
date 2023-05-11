# The New Dimension of Data

![Promotional Image](./images/promo.gif)

This is the companion repository for the talk presented on May 11th in partnership with The Black Codes.

## System Requirements

- [Python version ~> 3](https://www.python.org/downloads/)

## Getting Started

1. Create Python Virtual Env and activate it

   ```shell
   python3 -m venv venv
   ```

   ```shell
   source ./venv/bin/activate
   ```

2. Set up your OpenAI Account and get a secret key

   You will also need access to the OpenAI api. To do so you will need to visit platform.openai.com to create an account.

   After you have access to the OpenAI Platform, generate an API Key from the `View API keys` page. You can access this page by clicking your avatar in the top-right navigation.

   You will then need to add the generated API Key to a .env file in the root of this directory. Copy the .env.example remove `.example` and you'll be all set.

3. Run an example

   ```shell
       python ./examples/{NAME_OF_EXAMPLE}.py
   ```

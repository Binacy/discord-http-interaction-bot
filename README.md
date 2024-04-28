<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<br />
<div align="center">
  <h3 align="center">Discord http Interaction Bot</h3>

  <p align="center">
    An awesome open source project to demonstrate usage of discord http interactions in python!
    <br />
    ·
    <a href="https://github.com/Binacy/discord-http-interaction-bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/Binacy/discord-http-interaction-bot/issues">Request Feature</a>
  </p>
</div>

## About The Project

This repository is an open source project to demonstrate the usage of discord http interactions in python.
There are many repos using discord gateway system to create bots, but this repo is different. This repo uses discord http interactions to create a bot. This is a very undiscovered feature of discord and is still underrated. This repo is created to demonstrate the usage of this feature.

Here's why:
* There's no repo on github that demonstrates the usage of discord http interactions in python.
* Everything in this repo is well documented and explained.
* This repo is open source and free to use.
* This repo is created to help people who are new to discord bots and want to learn how to create one.
* Http interactions can be used to host serverless bots, it saves us a lot of hosting resources and money.

A great example is Dyno bot on discord which is using gateway and http interactions both simontaneously to save hosting resources and money. You can do the same, just with some knowledge of python, discord http interactions and some creativity.

Of course, no one will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people have contributed to expanding this project!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [Fastapi](https://fastapi.tiangolo.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

1. Clone this repo on your local machine
  ```sh
  git clone https://github.com/Binacy/discord-http-interaction-bot
  ```
2. Install the requirements (Sorry i use reqs instead of requirements)
  ```sh
  pip3 install -U -r reqs.txt
  ```
3. Create a discord application and bot on [Discord Developer Portal](https://discord.com/developers/applications)
4. Rename the [example.env](https://github.com/Binacy/discord-http-interaction-bot/blob/main/src/example.env) file to .env
5. Complete the .env file with your bot token, application id and public key from the discord developer portal.
6. Edit commands in [commands.py](https://github.com/Binacy/discord-http-interaction-bot/blob/main/src/commands.py)
* Note: You will have to run upsert.py before main.py to upload your slash commands to discord.
7. Run the bot
  ```sh
  python3 main.py
  ```
8. Sorry, you are not done yet! you have to use a server like [ngrok](https://ngrok.com/) to start a local webserver.
9. Please install any server like ngrok and start a local webserver on port 3000.
  ```sh
  ngrok http 3000
  ```
10. Copy the https url from the ngrok terminal and paste it in the discord developer portal in the interaction section.
11. You are done! Now you can use your bot in any server you want.
12. Ah! not done yet, You can use web services like vercel to host your bot 24/7 for free. You can also use heroku.
13. This is serverless hosting so it wont cost you much :wink:

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

Distributed under the MIT License. See [LICENSE](https://github.com/Binacy/discord-http-interaction-bot/blob/main/LICENSE) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Discord - [@Binacy](https://discord.com/users/1211202988518146050)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgments

Special thanks to [Aditya](https://github.com/Xenofic) and [Amey](https://github.com/AmeyWale) for helping me with this project.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Binacy/discord-http-interaction-bot.svg?style=for-the-badge
[contributors-url]: https://github.com/Binacy/discord-http-interaction-bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Binacy/discord-http-interaction-bot.svg?style=for-the-badge
[forks-url]: https://github.com/Binacy/discord-http-interaction-bot/network/members
[stars-shield]: https://img.shields.io/github/stars/Binacy/discord-http-interaction-bot.svg?style=for-the-badge
[stars-url]: https://github.com/Binacy/discord-http-interaction-bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/Binacy/discord-http-interaction-bot.svg?style=for-the-badge
[issues-url]: https://github.com/Binacy/discord-http-interaction-bot/issues
[license-shield]: https://img.shields.io/github/license/Binacy/discord-http-interaction-bot.svg?style=for-the-badge
[license-url]: https://github.com/Binacy/discord-http-interaction-bot/LICENSE

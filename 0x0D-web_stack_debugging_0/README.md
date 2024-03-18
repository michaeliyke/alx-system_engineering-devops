# 0x0D. Web stack debugging #0

> This project was on ...
`DevOps` `Scripting` `SysAdmin` `Debugging`

## I learnt about

### General

- Webstack Debugging

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 14.04 LTS
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass `Shellcheck` (version `0.3.7`) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## Files

- 0-give_me_a_page

```terminal
#!/usr/bin/env bash
# The steps required to fix the Apache server
image="holbertonschool/265-0"
# Download the image
sudo docker pull "$image"
# Run the container detatched, and get its id
container_id=$(sudo docker run -d -it -p 8080:80 "$image")
# List the existing all running containers by their id
docker ps -q
# Statrt the apache2 service in the container and suppress its warnings
docker exec --privileged "$container_id" sudo service apache2 start > /dev/null 2>&1
# check that the apache2 service is running
curl 0.0.0.0:8080
```

> Each file contains the solution to a task in the project.

<!-- markdownlint-disable-next-line -->
#### Credits

Work is owned and maintained by [Michael C. Iyke](https://github.com/michaeliyke).

## Acknowledgement

All work contained in this project was completed as part of the curriculum for Alx. ALX is a leading technology training provider, built to accelerate the careers of young Africans through the technology and professional skills that enable them to thrive in the digital economy. The program prepares students for careers in the tech industry using project-based peer learning. For more information, [visit](https://www.alxafrica.com/).

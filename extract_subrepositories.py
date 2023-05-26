#########################################################################################
#
#  Copyright (c) 2023 ZF Friedrichshafen AG
#  Author: Rohan Krishnamurthy
#  E-mail: rohan.krishnamurthy@zf.com
#
#########################################################################################

import yaml

tractusx_file = ".tractusx"

with open(tractusx_file, "r") as file:
    data = yaml.safe_load(file)

repositories = data["repositories"]

with open("subrepositories.txt", "w") as file:
    for repository in repositories:
        file.write(repository["url"] + "\n")

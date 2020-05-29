# -- CheckOut -- 
------------------------------------------
This tool updates multiple git repositories based on a .json config file
## Requirements (optional)
+ Python or use the executable file from the release package
------------------------------------------
## The configuration file must be structured as follows
![not found](https://github.com/Soonkz/CheckOut/blob/master/github/config.PNG?raw=true)
------------------------------------------
# How to use:
+ Clone this repository at the same level as the other repositories
+ Create or copy CheckOut.json inside your repository
+ Enter all repositories you want to update with their repository names, TagOrBranch and Branch names

## The folder structure must look like this
------------------------------------------
- CheckOut
  - Checkout.py
  - Checkout.exe
  - ...
- RepoWithConfig
  - CheckOut.json
  - ...
- FirstRepo
  - ...
- SecondRepo
  - ...
- n...
------------------------------------------
## Execute CheckOut

```
Checkout.exe RepoWithConfig
```
or 
```
python Checkout.py RepoWithConfig
```
------------------------------------------
![not found](https://github.com/Soonkz/CheckOut/blob/master/github/execute.gif?raw=true)

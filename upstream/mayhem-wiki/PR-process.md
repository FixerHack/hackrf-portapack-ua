
## Create a PR

Before you are able to create a PR, you need to fork the Mayhem-Firmware Repository (https://github.com/portapack-mayhem/mayhem-firmware/) to in your own GitHub Repository.  
If you are logged in Github, open the Mayhem-Firmware Repository, at the top right you'll find the button `fork`. Click on `create new fork`.  

Now you need to download your own fork to your computer: `git clone https://github.com/<own username>/mayhem-firmware/ --recursive`.  
Now work on the cloned fork of the repository, as usual. Just add/commit the changes. Make sure you are adding meaningful descriptions at each commit.  

After some changes You go back to the browser and open the mayhem-firmware project in your repository.  
If you synced your changes with the fork in your repository, on the top of of the code will appear: `This branch is [7 commits ahead of], [6 commits behind] portapack-mayhem/mayhem-firmware:next.`  
Click on `[7 commits ahead of]` and the green Button `Create Pull Request` will appear.  

Now you are working in the PortaPack-Mayhem repository. Just follow the instructions and give a meaningful description in your PR.  
The approval/merge process starts.

### Option for expert
We’ve simplified the process in guide above. It usually works good and harmless if you just want to do small changes.
However if you want to make it more clear, you should do code change in a new branch, instead of the default branch “next”, follow this:
1. Fork the repo, clone the fork into local, settle submodules.
2. In the local repo dir:
```
git checkout next
git pull
git checkout -b branch_name
```
3. Do code change, do test
4. When ready to make PR:
```
git add -A
# or only add those that you wanted it to append into PR.
git commit -m “what you changed”
git push -u origin branch_name
```
5. Do PR on GitHub website.

> [!NOTE]
Q: What if I already did change in next branch but now I want to go “expert” way?  
A: cherry-pick your commute from next to your new branch, then push your new branch, after all done, reset your next or sync your next on GitHub webpage.

## Merge Process

In order to get your PR merged into the code base, there are a few checks that need to happen first.

* At least one code approver needs to approve your code. 
* If any code reviewer left PR comments, then all those PR comments left by reviewers need to be marked as resolved.
* All 3 code format gate checks need to complete successfully. (don't know how to format your code? Check out how to do it here https://github.com/portapack-mayhem/mayhem-firmware/wiki/Code-formatting) 

Once these steps are all complete, if you are an approved contributor you will notice you have a green merge button available, then means you are good to go and merge your code into the code base. Everyone else will see that tests have passed and will need to ask an approved contributor to merge it in for them (You can as the dev that approved the changes).

If any of these steps are not complete or failed, then you will be blocked from merging your code until they have all been completed.

### Usernames on the nightly change log
A new build of 'next' is released every night. Your contribution will be added to the list of changes that were accepted that day.
In order for your user account to display correctly you must either.
Enable 'Keep my email addresses private' which will add a unique email address like '417283+YourGitHubUser@noreply...'. Your username will be extracted from the private no-reply email address.

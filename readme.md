# NXT workspace

Since we are using a lot of packages to develope the nxt backend services and compilers, it's quite tricky to clone all of them and start installing them one by one, needless to say the headache of linking and publishing the packages once all of our work is done.

The workspace will help us automate most of our work that we do manually, starting from development to publishing the packages.

## Cloning the workspace

Since you might think that **git clone** will work out of the box, let me say that's not the case!

For this workspace we are using git **submodules,** git will not clone the submodules unless you specifiy that, it will only add them in your project without their contents.

So instead of the regular clone you need to execute the following command:

```bash
git clone git@github.com:monajjar1/nxt-workspace.git --recurse-submodules
```

This will tell git to clone the repo, with it's submodules and their content.

# GIT 笔记
## 安装git
    sudo apt-get install git

    git config --global user.name: 'username'

    git config --global user.email: 'email'

>git config global 选项表示本机器上所有的仓库都会使用这个该配置。

## 创建版本库
>什么是版本库呢？ 其实版本库就是一个目录，该目录下的所有文件都会被git控制，对该目录下任何文件的修改，增加，删除都会被git记录，方便我们随时对文件修改情况进行跟踪，复原。

在一个目录下使用`git init`就可以建版本库啦

    mkdir learngit
    cd learngit
    git init

## 把文件放入版本库
>git只能跟踪文本文件的变化，比如某行修改了那些字符。对于图片，视频，音频这些二进制文件，git只能记录文件的变化信息，比如更新日期，但到底更改，添加或删除了文件的那部分内容，git就文能为力了。

    cd learngit
    git add 'new file'
    git commit -m "一下关于本次修改的描述"

## 查看文件的修改情况
`git status` 告诉你哪些文件被改动了。

`git diff`   告诉你文件的哪一行到底被改成了什么样。
>提交更新和把新文件放入版本库都是相同的步骤，
>
> `git add <file>`
>
> `git commit -m "description"`


## 查看修改日志，“我都干了什么”
`git log [--pretty=oneline]` 告诉你，你这段时间都干了些什么。

`git reflog`  记录你每次更改的commit id， 你干的任何事git都为你记录在案了，并分配了一个id标记，哈哈。

## 版本回溯， *回到未来*
`git reset --hard <commit id>`

## 几个概念
### 工作区
就是我们在自己机器上创建的目录，比如`~/software/document`
### 版本库
工作区下面有一个隐藏文件夹.git，这个隐藏目录就是版本库
### 暂存区
在版本库下面有一个叫index的文件，它就是暂存区。
### `git add <file>`和`git commit`干了些什么
`git add`将我们对文件的修改放到暂存区中, `git commit`将暂存区里的内容存，也就是我们对工作区中文件的修改到master分支中。

![git add][add]

![git commit] [commit]

[add]: ./add.jpg
[commit]: ./commit.jpg

>[git 跟踪的是修改，而不是文件本身](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/001374829472990293f16b45df14f35b94b3e8a026220c5000)

## 撤销修改， *我有反悔的权力*

1. 只是在工作区里修改了，还没add到暂存区，我反悔了

   `git checkout -- <file>`
   >如果暂存区里是空的，这一步会把工作区的状态变回与版本库里的状态一样，即你上一次commit的状态。

   >如果暂存区里有内容，这一步会把工作区的状态变回与暂存区里的状态一样。

2. 在工作区修改了，add到暂存区了，可是我反悔了

  `git reset HEAD <file>`

  `git checkout -- <file>`

3. 已经讲修改commit到版本库里了,我反悔了

  还记得版本回溯吗。

4. 已经把文件提交到远程库里了，我反悔了

   *希望你平时的人缘不错....*

## 从版本库中删除文件

`git rm <file>`

`git commit`

## 远程仓库
把本地的版本仓库推送到github
* 在自己的家目录下`～/`创建以对ssh key

    `ssh-keygen -t rsa -C "your email"`
* 在你的github个人账户页面的ssh选项下，增添你生成的ssh key

   ![github ssh][sshkey]

[sshkey]:./github_sshkey.png
>放到github上，任何和都可以看到你的版本库了，因为设置了sshkey，别人只能看，不能修改。

* 在github上新建一个版本库

    ![github new repository][]

[github new repository]: ./github_new_repository.png

* 把本地版本库和github上的远程库关联起来

    在工作区目录下`~/document`运行命令：

    `git remote add origin https://github.com/FengYusheng/document.git`

>github会给出提示的。

* 将本地版本库推送到github
  `git push -u orgin master`

>第一次推送要有`-u`, github会有提示的

## 从远程仓库克隆代码到本地版本库
`git clone <url>`

> url有https和ssh两种协议，比如：

> "https://github.com/FengYusheng/document.git"

> "git@github.com:FengYusheng/document.git"

## 分支管理， *神奇的平行宇宙*
* 创建分支： `git branch <name>`
* 切换分支: `git checkout <name>`
* 创建并切换分支: `git checkout -b <name>`
* 合并某分支到当前分支： `git merge <name>`
* 删除某分支： `git branch -d <name>`
* 把暂不打算提交的工作暂存，*保护现场* : `git stash`

>[分支管理][]， 神奇的平行宇宙

[分支管理]: http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/0013760174128707b935b0be6fc4fc6ace66c4f15618f8d000

## 标签管理， *让我为你拍张照*
`git tag <name>` 默认在HEAD 上打标签。

`git tag <name> [commit id]` 在指定commit id 上打标签。

`git tag -d <name>` 删除一个本地标签。

`git push origin <tag name>` 推送一个本地标签。

`git push origin --tags` 推送全部尚未推送过的本地标签。

## 使用github

[使用github][]

[使用github]: http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/00137628548491051ccfaef0ccb470894c858999603fedf000


![fork and pull request][]

[fork and pull request]: ./github_fork.png

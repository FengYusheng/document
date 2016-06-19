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

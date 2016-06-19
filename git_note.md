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
`git status` 显示哪些文件被改动了。

`git diff`显示文件的哪一行具体被改成了什么样。

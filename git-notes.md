# 前言
本笔记记录git学习过程中的全部资料及个人总结.  
学习教程:[廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/896043488029600)
- - - - 
  
# git 初始化
## 本地仓库与github同步
### 通过SSH同步
[创建本地仓库,提交至github](https://www.cnblogs.com/geeksongs/p/10606906.html)  
[通过SSH链接到github](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh)
[查询已经存在的SSH-KEY](https://docs.github.com/en/github/authenticating-to-github/checking-for-existing-ssh-keys)  
[创建新的SSH-KEY,添加至SSH代理](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)  
[在Github上添加新的SSH-key](https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account)  
[给SSH-key上秘钥](https://docs.github.com/en/github/authenticating-to-github/working-with-ssh-key-passphrases)  
#### 同步步骤注意事项
1. 先做 git pull 把数据从远程服务器拉到本地,然后再执行修改;  
   `$ git pull -f origin master`
2. 编辑完成后,通过git status进行检查  
   `$ git status`
3. 检查完成后,通过 git rm XXX 删除对应文件,通过 Git add 添加文件;  
   `$ git rm readme.txt`
4. 最后,通过 git push 把数据重新推到远程服务器.  
   `$ git push origin master`
   > 如果git push报如下错误,表示一开始没有把数据拉到本地,需要把修改的部分移走,然后把数据拉回本地,再执行步骤2-4.
   ```
   To github.com:cnzh2020/gitlearning.git ! [rejected]        master -> master (non-fast-forward)  
    error: failed to push some refs to 'github.com:cnzh2020/gitlearning.git'
    hint: Updates were rejected because the tip of your current branch is behind
    hint: its remote counterpart. Integrate the remote changes (e.g.
    hint: 'git pull ...') before pushing again.
    hint: See the 'Note about fast-forwards' in 'git push --help' for details.
   ```
   > 如果不执行步骤2-4需要强制推数据,使用 -f 强制上推文件至远程服务器,强制上推后,远程服务器的文件会被强制刷新  
   `$ git push -f origin master`
#### 分支合并出现问题
[Git Error 因文件出错导致上传被打断](https://blog.csdn.net/shizhenweiszw/article/details/87486195)  
[Git push 远程服务器文件冲突报错](https://blog.csdn.net/weixin_43290229/article/details/86410263)
#### git访问速度过慢的处理
[解决git网络访问过慢](https://blog.csdn.net/zhaojieip/article/details/88702947)

### 通过https同步
[使用git将项目上传到github](https://www.cnblogs.com/cxk1995/p/5800196.html)
## Git Shell
Gitshell属于一种命令编辑器,是linux的外壳,Git bash属于其中一种.  
[GitBash介绍及语法](https://blog.csdn.net/goog_man/article/details/95044688)


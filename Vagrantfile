Vagrant.configure("2") do |config|

     config.vm.define "centos" do |centos|
       centos.vm.box = "centos/7"

       config.vm.network "private_network", ip: "192.168.33.10"

       config.vm.provision "shell", inline: <<-SHELL
         sudo yum -y update
         sudo yum -y install yum-utils
         sudo yum -y groupinstall development
         sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm
         sudo yum -y install python36u
       SHELL

       config.vm.provision "shell",
       inline: "sudo /usr/bin/python3.6 /vagrant/socket_listen.py &",
       run: "always"

    end
end

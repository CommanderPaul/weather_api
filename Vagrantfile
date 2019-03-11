# https://medium.com/@Joachim8675309/vagrant-provisioning-with-puppet-553a59f0c48e

Vagrant.configure("2") do |config|

  config.vm.box = "geerlingguy/centos7" # has guest additions
  #config.vm.box = "bento/centos-7.6"
  #config.vm.network "forwarded_port", guest: 80, host: 8084
  config.vm.hostname = "weatherman"
  config.vm.network "private_network", ip: "192.168.33.10"


  ####### Install Puppet Agent #######
  config.vm.provision "shell", path: "./bootstrap.sh"

  ####### Provision #######
  config.vm.provision "puppet" do |puppet|
    puppet.module_path = ["./site"]
    #puppet.options = "--verbose --debug"
  end
end

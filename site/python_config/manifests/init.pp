class python_config {

package { 'yum-utils':
  ensure => present,
}

# installs, but is not idempotent - another bug
package { 'epel-release-7-11.noarch':
  ensure => present,
}


# installs, but is not idempotent - another bug
package { 'ius-release.rpm':
            provider => 'rpm',
            ensure   => installed,
            source => 'https://centos7.iuscommunity.org/ius-release.rpm',
}

package { ['python36u', 'python36u-devel', 'python36u-pip']:
  ensure => present,
}

# fix for below bug
file { '/usr/bin/pip3':
  ensure => 'link',
  target => '/usr/bin/pip3.6',
}

# bug where centos calls it pip3.6
package { ['requests']:
  ensure => present,
  provider => pip3,
  require => Package['python36u-pip'],
}


file {
    '/vagrant/http_server.py':
      ensure => 'file',
      path => '/vagrant/http_server.py',
      owner => 'vagrant',
      group => 'vagrant',
      mode  => '0755', # Use 0700 if it is sensitive
      notify => Exec['http_server_program'],
  }
exec { 'http_server_program':
  command => "/bin/python3.6 '/vagrant/http_server.py' &",
}



}

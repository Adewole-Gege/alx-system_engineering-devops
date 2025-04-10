# 1-user_limit.pp
# This Puppet manifest increases the file open limit for the 'holberton' user.

exec { 'increase_holberton_hard_limit':
  command => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 5000/g" /etc/security/limits.conf',
  unless  => 'grep "holberton hard nofile 5000" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/:/usr/bin/',
}

exec { 'increase_holberton_soft_limit':
  command => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 4000/g" /etc/security/limits.conf',
  unless  => 'grep "holberton soft nofile 4000" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/:/usr/bin/',
}
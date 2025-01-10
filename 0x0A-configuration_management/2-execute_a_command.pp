# This manifest kills the 'killmenow' process
exec { 'kill_killmenow_process':
  command => '/usr/bin/pkill -f killmenow',
  path    => ['/usr/bin', '/bin'],
  onlyif  => '/usr/bin/pgrep -f killmenow',
}

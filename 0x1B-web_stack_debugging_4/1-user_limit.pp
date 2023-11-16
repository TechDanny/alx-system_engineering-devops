# fix error messages

exec { 'replace-1':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 5000/" /etc/security/limits.conf',
  before   => Exec['replace-2'],
}

exec { 'replace-2':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 4000/" /etc/security/limits.conf',
}

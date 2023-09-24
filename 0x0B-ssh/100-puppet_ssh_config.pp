# client configuration with puppet

file_line{'login with no password':
path => '/etc/ssh/ssh_config',
line => 'PasswordAuthentication no',
}

file_line{'show identity':
path => '/etc/ssh/ssh_config',
line => 'IdentityFile ~/.ssh/school',
}

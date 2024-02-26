# Using Puppet to create a file and ensure it has a specific content
include stdlib

file_line { '/etc/ssh/ssh_config':
    line               => '    IdentityFile ~/.ssh/school',
    match              => '^[#]+[\s]*(?!)IdentityFile[\s]+~/.ssh/id_rsa$',
    replace            => true,
    append_on_no_match => true,
}

file_line { '/etc/ssh/ssh_config':
    line               => '    PassordAuthentication no',
    match              => '^[#]+[\s]*(?!)PassordAuthentication[\s]+(yes|no)$',
    replace            => true,
    append_on_no_match => true,
}

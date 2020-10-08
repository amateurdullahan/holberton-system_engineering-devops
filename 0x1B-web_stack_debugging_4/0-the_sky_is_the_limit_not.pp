#!/usr/bin/env bash
# fixinx nginx
exec { 'fix--for-nginx':
  command => "sed -i '5c ULIMIT=\"-n 4096\"' /etc/default/nginx && sudo service nginx restart",
  path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}

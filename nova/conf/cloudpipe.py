# needs:check_opt_group_and_type

# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_config import cfg

from nova.conf import paths

cloudpipe_opts = [
    cfg.StrOpt(
        'vpn_image_id',
        default='0',
        help="""
Image ID used when starting up a cloudpipe VPN client.

An empty instance is created and configured with OpenVPN using
boot_script_template. This instance would be snapshotted and stored
in glance. ID of the stored image is used in 'vpn_image_id' to
create cloudpipe VPN client.

Possible values:

* Any valid ID of a VPN image
"""),
    cfg.StrOpt(
        'vpn_flavor',
        default='m1.tiny',
        help="""
Flavor for VPN instances.

Possible values:

* Any valid flavor name
"""),
    cfg.StrOpt(
        'boot_script_template',
        default=paths.basedir_def('nova/cloudpipe/bootscript.template'),
        help="""
Template for cloudpipe instance boot script.

Possible values:

* Any valid path to a cloudpipe instance boot script template

Related options:
Following options are required to configure cloudpipe-managed
OpenVPN server.
* dmz_net
* dmz_mask
* cnt_vpn_clients
"""),
    cfg.IPOpt(
        'dmz_net',
        default='10.0.0.0',
        help="""
Network to push into OpenVPN config.

Note: Above mentioned OpenVPN config can be found at
/etc/openvpn/server.conf.

Possible values:

* Any valid IPv4/IPV6 address

Related options:
dmz_net is pushed into bootscript.template to configure
cloudpipe-managed OpenVPN server
* boot_script_template
"""),
    cfg.IPOpt(
        'dmz_mask',
        default='255.255.255.0',
        help="""
Netmask to push into OpenVPN config.

Possible values:

* Any valid IPv4/IPV6 netmask

Related options:
dmz_net and dmz_mask is pushed into bootscript.template to configure
cloudpipe-managed OpenVPN server
* dmz_net
* boot_script_template
"""),

    cfg.StrOpt(
        'vpn_key_suffix',
        default='-vpn',
        help="""
Suffix to add to project name for VPN key and secgroups

Possible values:

* Any string value representing the VPN key suffix
""")
]


def register_opts(conf):
    conf.register_opts(cloudpipe_opts)


def list_opts():
    # TODO(siva_krishnan) add opt group
    return {'DEFAULT': cloudpipe_opts}

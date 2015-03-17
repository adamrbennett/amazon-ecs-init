# Copyright 2014-2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the
# "License"). You may not use this file except in compliance
# with the License. A copy of the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and
# limitations under the License.

%define	init_dir /etc/init
%define bin_dir /opt/amazon
%define	conf_dir /etc/ecs
%define cache_dir /var/cache/ecs
%define data_dir /var/lib/ecs/data
Name:           ecs-init
Version:        0.3
Release:        0
Group:          System Environment/Base
Vendor:         Amazon.com
License:        Apache 2.0
Summary:        Amazon EC2 Container Service init application
BuildArch:      x86_64
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	ecs.conf
Source1:	amz-ecs-init

Requires:	docker
Requires:	upstart

%description
ecs-init is a service which may be run to register an EC2 instance as an Amazon
ECS Container Instance.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{init_dir}
mkdir -p $RPM_BUILD_ROOT/%{bin_dir}
mkdir -p $RPM_BUILD_ROOT/%{conf_dir}
mkdir -p $RPM_BUILD_ROOT/%{cache_dir}
mkdir -p $RPM_BUILD_ROOT/%{data_dir}

install %{SOURCE0} $RPM_BUILD_ROOT/%{init_dir}/ecs.conf
install %{SOURCE1} $RPM_BUILD_ROOT/%{bin_dir}/amz-ecs-init
touch $RPM_BUILD_ROOT/%{conf_dir}/ecs.config
touch $RPM_BUILD_ROOT/%{conf_dir}/ecs.config.json
touch $RPM_BUILD_ROOT/%{cache_dir}/ecs-agent.tar

%files
%defattr(-,root,root,-)
%{init_dir}/ecs.conf
%{bin_dir}/amz-ecs-init
%config(noreplace) %ghost %{conf_dir}/ecs.config
%config(noreplace) %ghost %{conf_dir}/ecs.config.json
%ghost %{cache_dir}/ecs-agent.tar
%dir %{data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Mar 16 2016 Samuel Karp <skarp@amazon.com) - 0.3-0
- Migrate to statically-compiled Go binary
* Tue Feb 17 2015 Eric Nordlund <ericn@amazon.com> - 0.2-3
- Test for existing container agent and force remove it
* Thu Jan 15 2015 Samuel Karp <skarp@amazon.com> - 0.2-2
- Mount data directory for state persistence
- Enable JSON-based configuration
* Mon Dec 15 2014 Samuel Karp <skarp@amazon.com> - 0.2-1
- Naive update functionality
* Thu Dec 11 2014 Samuel Karp <skarp@amazon.com> - 0.2-0
- Initial version

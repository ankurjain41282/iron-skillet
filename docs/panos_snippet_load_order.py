# This ordered dictionary does not use Panorama and goes direct to the firewall
# This is api type = firewall in the web portal

Panos_gold_template_dict = OrderedDict([
      ('shared_log_settings', ['shared_log_settings']),
      ('tag', ['tag']),
      ('device_system', ['device_system']),
      ('device_setting', ['device_setting']),
      ('address', ['address']),
      ('external_list', ['external_list']),
      ('profiles_custom_url_category', ['profiles_custom_url_category']),
      ('profiles_decryption', ['profiles_decryption']),
      ('profiles_file_blocking', ['profiles_file_blocking']),
      ('profiles_spyware', ['profiles_spyware']),
      ('profiles_url_filtering', ['profiles_url_filtering']),
      ('profiles_virus', ['profiles_virus']),
      ('profiles_vulnerability', ['profiles_vulnerability']),
      ('profiles_wildfire_analysis', ['profiles_wildfire_analysis']),
      ('profile_group', ['profile_group']),
      ('shared_log_settings_profiles', ['log_settings_profiles']),
      ('default_security_rules', ['rulebase_default_security_rules']),
      ('security_rules', ['rulebase_security']),
      ('decryption_rules', ['rulebase_decryption']),
      ('zone_protection_profile', ['zone_protection_profile']),
      ('shared_reports', ['reports_simple']),
      ('shared_report_group', ['report_group_simple']),
      ('shared_email_scheduler', ['email_scheduler_simple']),
                          ])
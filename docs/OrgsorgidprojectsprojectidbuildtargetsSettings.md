# OrgsorgidprojectsprojectidbuildtargetsSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_build** | **bool** | start builds automatically when your repo is updated | [optional] 
**unity_version** | **str** | &#x27;latest&#x27; or a unity dot version with underscores (ex. &#x27;4_6_5&#x27;) | [optional] 
**auto_detect_unity_version** | **bool** | attempt to automatically detect which unity version to use, fallback to specified unityVersion if unable to. | [optional] 
**fallback_patch_version** | **bool** | attempt to get a similar unity patch version to use, applies to unavailable auto-detected Unity versions only. | [optional] 
**executablename** | **str** |  | [optional] 
**scm** | [**OrgsorgidprojectsprojectidbuildtargetsSettingsScm**](OrgsorgidprojectsprojectidbuildtargetsSettingsScm.md) |  | [optional] 
**platform** | [**OrgsorgidprojectsprojectidbuildtargetsSettingsPlatform**](OrgsorgidprojectsprojectidbuildtargetsSettingsPlatform.md) |  | [optional] 
**build_schedule** | [**OrgsorgidprojectsprojectidbuildtargetsSettingsBuildSchedule**](OrgsorgidprojectsprojectidbuildtargetsSettingsBuildSchedule.md) |  | [optional] 
**auto_build_cancellation** | **bool** |  | [optional] [default to False]
**gcp_beta_opt_in** | **bool** |  | [optional] [default to False]
**gcp_opt_out** | **bool** |  | [optional] [default to False]
**operating_system_selected** | **str** |  | [optional] 
**ruby_version** | **str** |  | [optional] 
**advanced** | [**OrgsorgidprojectsprojectidbuildtargetsSettingsAdvanced**](OrgsorgidprojectsprojectidbuildtargetsSettingsAdvanced.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


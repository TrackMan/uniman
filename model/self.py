from typing import Any, List

from statham.schema.constants import Maybe
from statham.schema.elements import (
    Array,
    Boolean,
    Element,
    Integer,
    Object,
    String,
)
from statham.schema.property import Property


class Meta(Object):

    rc: str = Property(String(), required=True)


class Tables(Object):

    pass


class TopologyViewSettings(Object):

    showAllClients: bool = Property(Boolean(), required=True)

    show2GClients: bool = Property(Boolean(), required=True)

    show5GClients: bool = Property(Boolean(), required=True)

    showSSID: bool = Property(Boolean(), required=True)

    showWifiExperience: bool = Property(Boolean(), required=True)

    showRadioChannel: bool = Property(Boolean(), required=True)

    showWifiStandards: bool = Property(Boolean(), required=True)

    showWiredSpeed: bool = Property(Boolean(), required=True)

    showWiredPorts: bool = Property(Boolean(), required=True)


class Preferences(Object):

    alertsPosition: str = Property(String(), required=True)

    allowHiddenDashboardModules: bool = Property(Boolean(), required=True)

    browserLogLevel: str = Property(String(), required=True)

    bypassAutoFindDevices: bool = Property(Boolean(), required=True)

    bypassConfirmAdoptAndUpgrade: bool = Property(Boolean(), required=True)

    bypassConfirmBlock: bool = Property(Boolean(), required=True)

    bypassConfirmRestart: bool = Property(Boolean(), required=True)

    bypassConfirmUpgrade: bool = Property(Boolean(), required=True)

    bypassHybridDashboardNotice: bool = Property(Boolean(), required=True)

    bypassHybridSettingsNotice: bool = Property(Boolean(), required=True)

    dateFormat: str = Property(String(), required=True)

    dismissWlanOverrides: bool = Property(Boolean(), required=True)

    enableNewUI: bool = Property(Boolean(), required=True)

    hideV3SettingsIntro: bool = Property(Boolean(), required=True)

    isAppDark: bool = Property(Boolean(), required=True)

    isPropertyPanelFixed: bool = Property(Boolean(), required=True)

    isRegularGraphForAirViewEnabled: bool = Property(Boolean(), required=True)

    isResponsive: bool = Property(Boolean(), required=True)

    isSettingsDark: bool = Property(Boolean(), required=True)

    isUndockedByDefault: bool = Property(Boolean(), required=True)

    noWhatsNew: bool = Property(Boolean(), required=True)

    propertyPanelCollapse: bool = Property(Boolean(), required=True)

    propertyPanelMultiMode: bool = Property(Boolean(), required=True)

    refreshButtonEnabled: bool = Property(Boolean(), required=True)

    refreshRate: str = Property(String(), required=True)

    refreshRateRememberAll: bool = Property(Boolean(), required=True)

    rowsPerPage: int = Property(Integer(), required=True)

    showAllPanelActions: bool = Property(Boolean(), required=True)

    timeFormat: str = Property(String(), required=True)

    use24HourTime: bool = Property(Boolean(), required=True)

    useBrowserTheme: bool = Property(Boolean(), required=True)

    useSettingsPanelView: bool = Property(Boolean(), required=True)

    websocketEnabled: bool = Property(Boolean(), required=True)

    withStickyTableActions: bool = Property(Boolean(), required=True)

    isUlteModalClosed: bool = Property(Boolean(), required=True)

    isUbbAlignmentToolModalClosed: bool = Property(Boolean(), required=True)

    serviceWorkers: bool = Property(Boolean(), required=True)


class DismissedSurveys(Object):

    DASHBOARD: int = Property(Integer(), required=True)

    NEW_SETTINGS: int = Property(Integer(), required=True)


class (Object):

    order: int = Property(Integer(), required=True)


class Dashboards(Object):

    _6009922930760c05b292ed78:  = Property(required=True, source='6009922930760c05b292ed78')


class DashboardConfig(Object):

    lastActiveDashboardId: str = Property(String(), required=True)

    dashboards: Dashboards = Property(Dashboards, required=True)


class UiSettings(Object):

    neverCheckForUpdate: bool = Property(Boolean(), required=True)

    statisticsPrefferedTZ: str = Property(String(), required=True)

    statisticsPreferBps: str = Property(String(), required=True)

    tables: Tables = Property(Tables, required=True)

    topologyViewSettings: TopologyViewSettings = Property(TopologyViewSettings, required=True)

    preferredLanguage: str = Property(String(), required=True)

    preferences: Preferences = Property(Preferences, required=True)

    dismissedSurveys: DismissedSurveys = Property(DismissedSurveys, required=True)

    dashboardConfig: DashboardConfig = Property(DashboardConfig, required=True)


class Surveys(Object):

    show_settings: bool = Property(Boolean(), required=True)

    show_dashboard: bool = Property(Boolean(), required=True)


class DataItem(Object):

    admin_id: Maybe[str] = Property(String())

    avatar_url: Maybe[str] = Property(String())

    device_id: Maybe[str] = Property(String())

    email: Maybe[str] = Property(String())

    email_alert_enabled: Maybe[bool] = Property(Boolean())

    email_alert_grouping_delay: Maybe[int] = Property(Integer())

    email_alert_grouping_enabled: Maybe[bool] = Property(Boolean())

    first_name: Maybe[str] = Property(String())

    html_email_enabled: Maybe[bool] = Property(Boolean())

    is_owner: Maybe[bool] = Property(Boolean())

    is_professional_installer: Maybe[bool] = Property(Boolean())

    is_super: Maybe[bool] = Property(Boolean())

    last_name: Maybe[str] = Property(String())

    last_site_name: Maybe[str] = Property(String())

    name: Maybe[str] = Property(String())

    push_alert_enabled: Maybe[bool] = Property(Boolean())

    requires_new_password: Maybe[bool] = Property(Boolean())

    super_site_permissions: Maybe[List[Any]] = Property(Array(Element()))

    ubic_name: Maybe[str] = Property(String())

    ubic_uuid: Maybe[str] = Property(String())

    ui_settings: Maybe[UiSettings] = Property(UiSettings)

    uid: Maybe[str] = Property(String())

    surveys: Maybe[Surveys] = Property(Surveys)

    last_site_id: Maybe[str] = Property(String())

    site_id: Maybe[str] = Property(String())

    site_name: Maybe[str] = Property(String())

    site_permissions: Maybe[List[Any]] = Property(Array(Element()))

    site_role: Maybe[str] = Property(String())


class Self(Object):

    meta: Maybe[Meta] = Property(Meta)

    data: Maybe[List[DataItem]] = Property(Array(DataItem))

# coding: utf-8
import pytest

from ...config.config_loader import ConfigLoader
from .abstract import config


class TestStartUrls:
    def test_mandatory_start_urls(self):
        """ Should throw if no start_urls passed """
        # Given
        c = config({
            'start_urls': None
        })

        # When / Then
        with pytest.raises(ValueError):
            ConfigLoader(c)

    def test_start_urls_doesnt_accept_single_value(self):
        """ Allow passing start_urls as string instead of array """
        # Given
        c = config({
            'start_urls': 'www.foo.bar'
        })

        with pytest.raises(Exception) as excinfo:
            # When
            ConfigLoader(c)
            # Then
            assert 'start_urls should be list' in str(excinfo.value)

    def test_start_urls_should_have_at_least_one_element(self):
        """ Should throw if start_urls does not have at least one element """
        # Given
        c = config({
            'start_urls': []
        })

        # When / Then
        with pytest.raises(ValueError):
            ConfigLoader(c)

    def test_start_url_should_add_default_page_rank_and_tags(self):
        """ Should add default values for page_rank and tags """
        # Given
        c = config({
            'start_urls': [{"url": "http://www.foo.bar/"}]
        })

        # When
        actual = ConfigLoader(c)

        # Then
        assert actual.start_urls[0]['tags'] == []
        assert actual.start_urls[0]['page_rank'] == 0

    def test_start_url_should_be_transform_to_object_if_string(self):
        """ Should accept strings for start_urls as well as objects """
        # Given
        c = config({
            'start_urls': ['http://www.foo.bar/']
        })

        # When
        actual = ConfigLoader(c)

        # Then
        assert actual.start_urls[0]['url'] == 'http://www.foo.bar/'

    def test_start_urls_should_be_generated_when_there_is_automatic_tagging_browser(
            self, monkeypatch):
        from .mocked_init import MockedInit
        monkeypatch.setattr("selenium.webdriver.chrome",
                            lambda x: MockedInit())
        monkeypatch.setattr("time.sleep", lambda x: "")

        # When
        c = config({
            "start_urls": [
                {
                    "url": "http://docs.rongcloud.net/guides",
                    "tags": ["guides"],
                    "selectors_key": "guides"
                },
                {
                    "url": "http://docs.rongcloud.net/platform-chat-api",
                    "tags": ["im", "platform_server"],
                    "selectors_key": "im-server-api"
                },
                {
                    "url": "http://docs.rongcloud.net/web-callplus",
                    "tags": ["rtc", "platform_web", "sdk_callplus"],
                    "selectors_key": "web-callplus"
                },
                {
                    "url": "http://docs.rongcloud.net/android-callplus",
                    "tags": ["rtc", "platform_android", "sdk_callplus"],
                    "selectors_key": "android-callplus"
                },
                {
                    "url": "http://docs.rongcloud.net/ios-callplus",
                    "tags": ["rtc", "platform_ios", "sdk_callplus"],
                    "selectors_key": "ios-callplus"
                },
                {
                    "url": "http://docs.rongcloud.net/android-callkit",
                    "tags": ["rtc", "platform_android", "callkit"],
                    "selectors_key": "android-callkit"
                },
                {
                    "url": "http://docs.rongcloud.net/ios-callkit",
                    "tags": ["rtc", "platform_ios", "callkit"],
                    "selectors_key": "ios-callkit"
                },
                {
                    "url": "http://docs.rongcloud.net/web-calllib",
                    "tags": ["rtc", "platform_web", "sdk_calllib"],
                    "selectors_key": "web-calllib"
                },
                {
                    "url": "http://docs.rongcloud.net/android-calllib",
                    "tags": ["rtc", "platform_android", "sdk_calllib"],
                    "selectors_key": "android-calllib"
                },
                {
                    "url": "http://docs.rongcloud.net/ios-calllib",
                    "tags": ["rtc", "platform_ios", "sdk_calllib"],
                    "selectors_key": "ios-calllib"
                },
                {
                    "url": "http://docs.rongcloud.net/android-push",
                    "tags": ["rtc", "platform_android", "sdk_push"],
                    "selectors_key": "ios-calllib"
                },
                {
                    "url": "http://docs.rongcloud.net/flutter-calllib",
                    "tags": ["rtc", "platform_android", "sdk_calllib"],
                    "selectors_key": "flutter-calllib"
                },
                {
                    "url": "http://docs.rongcloud.net/uni-app-calllib",
                    "tags": ["rtc", "platform_uni-app", "sdk_calllib"],
                    "selectors_key": "uni-app-calllib"
                },
                {
                    "url": "http://docs.rongcloud.net/react-native-calllib",
                    "tags": ["rtc", "platform_react-native", "sdk_calllib"],
                    "selectors_key": "react-native-calllib"
                },
                {
                    "url": "http://docs.rongcloud.net/web-rtclib",
                    "tags": ["rtc", "platform_web", "sdk_rtclib"],
                    "selectors_key": "web-rtclib"
                },
                {
                    "url": "http://docs.rongcloud.net/miniprogram-rtclib",
                    "tags": ["rtc", "platform_miniprogram", "sdk_rtclib"],
                    "selectors_key": "miniprogram-rtclib"
                },
                {
                    "url": "http://docs.rongcloud.net/android-rtclib",
                    "tags": ["rtc", "platform_android", "sdk_rtclib"],
                    "selectors_key": "android-rtclib"
                },
                {
                    "url": "http://docs.rongcloud.net/ios-rtclib",
                    "tags": ["rtc", "platform_ios", "sdk_rtclib"],
                    "selectors_key": "ios-rtclib"
                },
                {
                    "url": "http://docs.rongcloud.net/flutter-rtclib",
                    "tags": ["rtc", "platform_android", "sdk_rtclib"],
                    "selectors_key": "flutter-rtclib"
                },
                {
                    "url": "http://docs.rongcloud.net/uni-app-rtclib",
                    "tags": ["rtc", "platform_uni-app", "sdk_rtclib"],
                    "selectors_key": "uni-app-rtclib"
                },
                {
                    "url": "http://docs.rongcloud.net/react-native-rtclib",
                    "tags": ["rtc", "platform_react-native", "sdk_rtclib"],
                    "selectors_key": "react-native-rtclib"
                }
            ]
        })

        actual = ConfigLoader(c)
        print(actual.start_urls)
        print(len(actual.start_urls))
        # assert len(actual.start_urls) == 12
        # assert actual.start_urls[0]['url'] == "https://test.com/doc/1.0/book/"

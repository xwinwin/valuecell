"""Unit tests for YFinanceAdapter proxy configuration."""

from unittest.mock import MagicMock, patch

import pytest

from valuecell.adapters.assets.yfinance_adapter import YFinanceAdapter


class TestYFinanceAdapterProxy:
    """Test YFinanceAdapter proxy configuration."""

    @patch("valuecell.adapters.assets.yfinance_adapter.yf")
    def test_proxy_url_set_when_provided(self, mock_yf):
        """Verify YFinanceAdapter correctly sets the yfinance proxy when a PROXY_URL is provided."""
        # Arrange
        test_proxy_url = "http://proxy.example.com:8080"
        mock_yf.set_config = MagicMock()

        # Act
        adapter = YFinanceAdapter(proxy_url=test_proxy_url)

        # Assert
        mock_yf.set_config.assert_called_once_with(proxy=test_proxy_url)
        assert adapter.proxy_url == test_proxy_url

    @patch("valuecell.adapters.assets.yfinance_adapter.yf")
    def test_proxy_url_not_set_when_none(self, mock_yf):
        """Verify YFinanceAdapter does not set the yfinance proxy when no PROXY_URL is provided."""
        # Arrange
        mock_yf.set_config = MagicMock()

        # Act
        adapter = YFinanceAdapter(proxy_url=None)

        # Assert
        mock_yf.set_config.assert_not_called()
        assert adapter.proxy_url is None

    @patch("valuecell.adapters.assets.yfinance_adapter.yf")
    def test_proxy_url_not_set_when_empty_string(self, mock_yf):
        """Verify YFinanceAdapter does not set the yfinance proxy when PROXY_URL is empty."""
        # Arrange
        mock_yf.set_config = MagicMock()

        # Act
        adapter = YFinanceAdapter(proxy_url="")

        # Assert
        mock_yf.set_config.assert_not_called()
        assert adapter.proxy_url == ""

    @patch("valuecell.adapters.assets.yfinance_adapter.yf")
    def test_proxy_url_with_authentication(self, mock_yf):
        """Verify YFinanceAdapter handles proxy URLs with authentication."""
        # Arrange
        test_proxy_url = "http://user:password@proxy.example.com:8080"
        mock_yf.set_config = MagicMock()

        # Act
        adapter = YFinanceAdapter(proxy_url=test_proxy_url)

        # Assert
        mock_yf.set_config.assert_called_once_with(proxy=test_proxy_url)
        assert adapter.proxy_url == test_proxy_url

    @patch("valuecell.adapters.assets.yfinance_adapter.yf")
    def test_proxy_url_https(self, mock_yf):
        """Verify YFinanceAdapter handles HTTPS proxy URLs."""
        # Arrange
        test_proxy_url = "https://secure-proxy.example.com:8443"
        mock_yf.set_config = MagicMock()

        # Act
        adapter = YFinanceAdapter(proxy_url=test_proxy_url)

        # Assert
        mock_yf.set_config.assert_called_once_with(proxy=test_proxy_url)
        assert adapter.proxy_url == test_proxy_url

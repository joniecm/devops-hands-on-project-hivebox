import os
import unittest
from unittest.mock import patch

from src.config import MinioConfig, _get_bool_env, load_minio_config


class TestConfig(unittest.TestCase):
    """Test cases for config helpers."""

    def test_get_bool_env_default_false_when_missing(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertFalse(_get_bool_env("MISSING_FLAG"))

    def test_get_bool_env_default_true_when_missing(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertTrue(_get_bool_env("MISSING_FLAG", default=True))

    def test_get_bool_env_truthy_values(self):
        truthy_values = ["1", "true", "yes", "y", "on", " TRUE "]
        for value in truthy_values:
            with self.subTest(value=value):
                with patch.dict(os.environ, {"FLAG": value}, clear=True):
                    self.assertTrue(_get_bool_env("FLAG"))

    def test_get_bool_env_falsy_values(self):
        falsy_values = ["0", "false", "no", "n", "off", "", "  "]
        for value in falsy_values:
            with self.subTest(value=value):
                with patch.dict(os.environ, {"FLAG": value}, clear=True):
                    self.assertFalse(_get_bool_env("FLAG"))

    def test_load_minio_config_missing_required_returns_none(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertIsNone(load_minio_config())

    def test_load_minio_config_defaults(self):
        env = {
            "MINIO_ENDPOINT": "minio:9000",
            "MINIO_ACCESS_KEY": "access",
            "MINIO_SECRET_KEY": "secret",
            "MINIO_BUCKET": "temps",
        }
        with patch.dict(os.environ, env, clear=True):
            config = load_minio_config()

        self.assertIsInstance(config, MinioConfig)
        self.assertTrue(config.secure)
        self.assertIsNone(config.region)
        self.assertFalse(config.create_bucket)
        self.assertEqual(config.timeout, 5.0)

    def test_load_minio_config_overrides(self):
        env = {
            "MINIO_ENDPOINT": "minio:9000",
            "MINIO_ACCESS_KEY": "access",
            "MINIO_SECRET_KEY": "secret",
            "MINIO_BUCKET": "temps",
            "MINIO_SECURE": "false",
            "MINIO_REGION": "us-east-1",
            "MINIO_CREATE_BUCKET": "yes",
            "MINIO_TIMEOUT": "7.5",
        }
        with patch.dict(os.environ, env, clear=True):
            config = load_minio_config()

        self.assertIsInstance(config, MinioConfig)
        self.assertFalse(config.secure)
        self.assertEqual(config.region, "us-east-1")
        self.assertTrue(config.create_bucket)
        self.assertEqual(config.timeout, 7.5)


if __name__ == "__main__":
    unittest.main()

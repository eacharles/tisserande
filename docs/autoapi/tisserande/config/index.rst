tisserande.config
=================

.. py:module:: tisserande.config

.. autoapi-nested-parse::

   Configuration for tisserande, loaded from environment variables.



Attributes
----------

.. autoapisummary::

   tisserande.config.config


Classes
-------

.. autoapisummary::

   tisserande.config.TrackingConfiguration
   tisserande.config.DatabaseConfiguration
   tisserande.config.Configuration


Module Contents
---------------

.. py:class:: TrackingConfiguration(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for the provenance tracking system.


   .. py:attribute:: enabled
      :type:  bool
      :value: None



   .. py:attribute:: backend
      :type:  str
      :value: None



   .. py:attribute:: auto_classify
      :type:  bool
      :value: None



.. py:class:: DatabaseConfiguration(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Database configuration for tisserande.


   .. py:attribute:: url
      :type:  str
      :value: None



   .. py:attribute:: echo
      :type:  bool
      :value: None



.. py:class:: Configuration(_case_sensitive: bool | None = None, _nested_model_default_partial_update: bool | None = None, _env_prefix: str | None = None, _env_prefix_target: pydantic_settings.sources.EnvPrefixTarget | None = None, _env_file: pydantic_settings.sources.DotenvType | None = ENV_FILE_SENTINEL, _env_file_encoding: str | None = None, _env_ignore_empty: bool | None = None, _env_nested_delimiter: str | None = None, _env_nested_max_split: int | None = None, _env_parse_none_str: str | None = None, _env_parse_enums: bool | None = None, _cli_prog_name: str | None = None, _cli_parse_args: bool | list[str] | tuple[str, Ellipsis] | None = None, _cli_settings_source: pydantic_settings.sources.CliSettingsSource[Any] | None = None, _cli_parse_none_str: str | None = None, _cli_hide_none_type: bool | None = None, _cli_avoid_json: bool | None = None, _cli_enforce_required: bool | None = None, _cli_use_class_docs_for_groups: bool | None = None, _cli_exit_on_error: bool | None = None, _cli_prefix: str | None = None, _cli_flag_prefix_char: str | None = None, _cli_implicit_flags: bool | Literal['dual', 'toggle'] | None = None, _cli_ignore_unknown_args: bool | None = None, _cli_kebab_case: bool | Literal['all', 'no_enums'] | None = None, _cli_shortcuts: collections.abc.Mapping[str, str | list[str]] | None = None, _secrets_dir: pydantic_settings.sources.PathType | None = None, _build_sources: tuple[tuple[pydantic_settings.sources.PydanticBaseSettingsSource, Ellipsis], dict[str, Any]] | None = None, **values: Any)

   Bases: :py:obj:`pydantic_settings.BaseSettings`


   Configuration for tisserande.

   Nested models may be consumed from environment variables named according to
   the pattern 'TISSERANDE__NESTED__FIELD'.


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].


   .. py:attribute:: db
      :type:  DatabaseConfiguration


   .. py:attribute:: tracking
      :type:  TrackingConfiguration


.. py:data:: config


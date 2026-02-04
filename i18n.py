# -*- coding: utf-8 -*-
"""
Simple i18n helper for OpenFilters.

Usage:
    - Call i18n.set_language("zh_CN") or "en" early in the startup.
    - Wrap all user-facing strings in _("...").
    - Keep translation keys = original English strings.
"""

try:
	import builtins  # type: ignore
except ImportError:  # pragma: no cover - Python 2 fallback
	import __builtin__ as builtins  # type: ignore

try:
	import user_config  # type: ignore
except ImportError:
	user_config = None  # type: ignore


class Translator(object):
	def __init__(self):
		# default language
		self._lang = "en"
		# translations[lang][original_text] = translated_text
		self.translations = {
			"zh_CN": {
				# 这里先给一些示例，后续会逐步补充
				# 菜单栏示例：
				"&File": "文件(&F)",
				"&Edit": "编辑(&E)",
				"&View": "视图(&V)",
				"&Help": "帮助(&H)",

				# 带快捷键的示例（注意保留 \tCtrl+N 部分）：
				"&New Project": "新建工程(&N)",
				"&Open Project": "打开工程(&O)",
				"&Save Project": "保存工程(&S)",
				"E&xit": "退出(&X)",

				# 对话框示例：
				"Optimization": "优化",
				"Target": "目标",
				"Target:": "目标：",
				"Cancel": "取消",
				"OK": "确定",
				"Apply": "应用",
				"Close": "关闭",

				# 提示信息示例：
				"Material not found": "未找到材料",
				"Do you want to save the current project before exiting?":
					"在退出之前要保存当前工程吗？",
				"Confirm Exit": "确认退出",
				"Error": "错误",
				"Warning": "警告",

				# 工具栏提示
				"Open": "打开",
				"Open a file": "打开文件",
				"Save": "保存",
				"Save current project": "保存当前工程",

				# 材料相关
				"Regular": "常规",
				"Mixture": "混合",
				"Constant": "常量",
				"Cauchy": "柯西",
				"Table": "表格",
				"Sellmeier": "塞尔迈耶",
				"Material error (%s): %s.": "材料错误（%s）：%s。",
				"Material error (%s).": "材料错误（%s）。",
				"Material does not exist": "材料不存在",
				"Impossible to open the file": "无法打开文件",
				"Cannot parse material because %s": "无法解析材料，因为 %s",
				"Multiple description in material": "材料描述重复",
				"Description must be on a single line": "描述必须在单行内",
				"Multiple definition in material": "材料定义重复",
				"Kind must be on a single line": "材料类型必须在单行内",
				"Kind must be regular or mixture": "材料类型必须为常规或混合",
				"Model must be on a single line": "模型必须在单行内",
				"Unknown material model!": "未知材料模型！",
				"Rate must be on a single line": "沉积速率必须在单行内",
				"Rate must be a float": "沉积速率必须为浮点数",
				"Rates must be floats": "沉积速率必须为浮点数",
				"Rates must be on a single line": "沉积速率必须在单行内",
				"Constants must be on multiple line": "常量必须为多行",
				"Constants must contain one description and one value": "常量必须包含一个描述和一个数值",
				"Constants values must be floats": "常量数值必须为浮点数",
				"Variables must be on multiple line": "变量必须为多行",
				"Variables must contain one description and a list of values": "变量必须包含一个描述和数值列表",
				"Variable values must be floats": "变量数值必须为浮点数",
				"Unknown keyword %s": "未知关键字 %s",
				"Missing information": "缺少必要信息",
				"A single value is necessary for constants": "常量必须为单一数值",
				"A single rate is necessary for regular material": "常规材料必须只有一个沉积速率",
				"Regular material cannot have variables": "常规材料不能有变量",
				"A list of rates must be provided for mixtures": "混合材料必须提供速率列表",
				"The number of rates must be equal to the number of properties": "速率数量必须等于属性数量",
				"Variable values must be lists": "变量数值必须为列表",
				"The number of variable values must be equal to the number of properties": "变量数值数量必须等于属性数量",
				"Invalid property format (%s)": "属性格式无效（%s）",
				"Invalid property format (there must be at least 2 mixtures)": "属性格式无效（至少需要 2 组混合）",
				"Invalid property format (there must be at least 2 mixtures and 2 wavelengths)": "属性格式无效（至少需要 2 组混合且至少 2 个波长）",
				"Invalid property format (first mixture number must be 0)": "属性格式无效（第一组混合编号必须为 0）",
				"Line %i of the file is formatted incorectly": "文件第 %i 行格式不正确",
				"The refractive index must be defined at least at 3 wavelengths": "折射率必须至少在 3 个波长点定义",
				"The refractive index is defined multiple times at the same wavelength": "同一波长的折射率被重复定义",

				# 模块加载
				"It was impossible to load the module %s. An exception occured and returned the value: %s.\n":
					"无法加载模块 %s。发生异常并返回值：%s。\n",
				"Could not find module %s. An exception occured and returned the value: %s.\n":
					"无法找到模块 %s。发生异常并返回值：%s。\n",
				"Could not extract the description from the module %s.\n":
					"无法从模块 %s 中提取描述。\n",
				"An error occured while creating the submodule %s of the module %s. An exception occured and returned the value:%s. Check that the description given in the module correspond to the functions.\n":
					"创建子模块 %s（模块 %s）时发生错误。发生异常并返回值：%s。请检查模块描述是否与函数对应。\n",

				# 命令行提示
				"%s is not a directory": "%s 不是目录",
				"%s is not readable": "%s 不可读",
				"change the user material directory": "更改用户材料目录",
			}
		}

	def set_language(self, lang):
		if not lang:
			return
		self._lang = lang

	def detect_language_from_config(self):
		"""Try to read language from user_config.language or user_config.LANG."""
		lang = None
		if user_config is not None:
			# 优先使用小写 language，如果没有再退回到大写 LANG
			lang = getattr(user_config, "language", None) or getattr(
				user_config, "LANG", None
			)
		if not lang:
			lang = "en"
		self._lang = lang

	def translate(self, text):
		"""Translate a string according to current language.

		Rules:
		- If language is 'en', return original text.
		- If translation exists, return it.
		- If no translation, fall back to original text.
		- For labels with accelerators, we may have to preserve the part after '\t'.
		"""
		if not text:
			return text
		lang = self._lang or "en"
		if lang == "en":
			return text

		lang_map = self.translations.get(lang, {})

		# 处理菜单快捷键形式："Label\tCtrl+N"
		if "\t" in text:
			base, accel = text.split("\t", 1)
			base_tr = lang_map.get(base, base)
			return "%s\t%s" % (base_tr, accel)

		return lang_map.get(text, text)


# 全局单例
_translator = Translator()


def init_from_config():
	"""Initialize language from user_config if available."""
	_translator.detect_language_from_config()


def set_language(lang):
	_translator.set_language(lang)


def _(text):
	"""Global translation function.

	This will be bound to builtins._ at startup, so other modules can just call _('Text').
	"""
	return _translator.translate(text)


def install_builtin():
	"""Install '_' into builtins so all modules can use it without explicit import."""
	builtins._ = _


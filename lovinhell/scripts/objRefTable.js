const C3 = self.C3;
self.C3_GetObjectRefTable = function () {
	return [
		C3.Plugins.TiledBg,
		C3.Plugins.Sprite,
		C3.Plugins.Text,
		C3.Plugins.Button,
		C3.Plugins.Button.Cnds.OnClicked,
		C3.Plugins.System.Acts.NextPrevLayout,
		C3.Plugins.System.Acts.GoToLayout
	];
};
self.C3_JsPropNameTable = [
	{TiledBackground: 0},
	{Sprite: 0},
	{Sprite2: 0},
	{Sprite3: 0},
	{Text: 0},
	{Button: 0},
	{Sprite4: 0},
	{Sprite5: 0},
	{Sprite6: 0},
	{Sprite7: 0},
	{criminal: 0},
	{River: 0},
	{idk: 0},
	{Button2: 0},
	{Sprite8: 0}
];

self.InstanceType = {
	TiledBackground: class extends self.ITiledBackgroundInstance {},
	Sprite: class extends self.ISpriteInstance {},
	Sprite2: class extends self.ISpriteInstance {},
	Sprite3: class extends self.ISpriteInstance {},
	Text: class extends self.ITextInstance {},
	Button: class extends self.IButtonInstance {},
	Sprite4: class extends self.ISpriteInstance {},
	Sprite5: class extends self.ISpriteInstance {},
	Sprite6: class extends self.ISpriteInstance {},
	Sprite7: class extends self.ISpriteInstance {},
	criminal: class extends self.IButtonInstance {},
	River: class extends self.IButtonInstance {},
	idk: class extends self.IButtonInstance {},
	Button2: class extends self.IButtonInstance {},
	Sprite8: class extends self.ISpriteInstance {}
}
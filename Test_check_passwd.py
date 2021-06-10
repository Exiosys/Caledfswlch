#!/usr/bin/env python
# coding=utf-8

import unittest
import strgen
from PassTrough import Passthrough
from EncrDecr import DebateME


class TestEncodePassword(unittest.TestCase):

    def test_valid_key(self):
        pt = Passthrough("./Mount", "clé")
        mdp = "mot de gors sepfeiwfnew"
        k = DebateME().encode_key(mdp)
        pt.key_int_file(k)
        self.assertTrue(pt.check_passwd(mdp))

    def test_empty_key(self):
        pt = Passthrough("./Mount", "clé")
        mdp = ""
        k = DebateME().encode_key(mdp)
        pt.key_int_file(k)
        self.assertTrue(pt.check_passwd(mdp))

    def test_valid_key_with_accent(self):
        pt = Passthrough("./Mount", "clé")
        mdp = "ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØŒŠþÙÚÛÜÝŸàáâãäåæçèéêëìíîïðñòóôõöøœšÞùúûüýÿ"
        k = DebateME().encode_key(mdp)
        pt.key_int_file(k)
        self.assertTrue(pt.check_passwd(mdp))

    def test_unvalid_key(self):
        pt = Passthrough("./Mount", "clé")
        mdp = "mot de passe"
        k = DebateME().encode_key(mdp)
        pt.key_int_file(k)
        self.assertFalse(pt.check_passwd("mauvais mot de passe"))

    def test_unvalid_key_with_all_special(self):
        pt = Passthrough("./Mount", "clé")
        mdp = "¢ß¥£™©®ª×÷±²³¼½¾µ¿¶·¸º°¯§…¤¦≠¬ˆ¨‰۩ ๑ ۞ ♥ ஐ • @ ღ ● ₪ √ ™ № ╬ ~ ξ € ﺕ ≈ ॐ ♪ ® ♂ ♀ û â î ♣ ♠ ◊ εїз ^ + * & % # ¨ o 0 »-> ø ¤ ? ¿ © † ♡ <-« ๏ ย ร ø ж ° ■ஹ ஸ ఋ ఊ ௌ ொஇ ౖ ௲ ூ ஃ ஊ ஏ ஐ ஒ ஓ ஔ ஜ ஞ ి ಔ ృ ూ ప ௯ ௮ ி ஞ ஜ ಋ ౡౠ ౖ ಱ ಯ ಮ ಭ ಬ ￼↔ ↕ ﻬ ҳ̸Ҳ̸ҳ ± Ψ۝ ╦ ╩ § ▲♦ ¶ ∩ $ ¼ ½ ¾ x » « ╚> <╝❤♫ ♬ ♪ ♩ ♭ ♪☀ஐღ♂♀♥♡☜☞☎☏♠♣▣▤▥▦▩♬♪♩♭♪の☆→あⓛⓞⓥⓔ｡°º¤•εïз╬㊈㊉㊊㊋㊌㊍㊎㊏㊐㊑㊒㊓㊔㊕㊖㊗⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㊀㊁㊂㊃㊄㊅㊆㊇㊈㊉㊊のஐღ♂ ♀ ♥ ♠ ♣ ♪ の ☆→ あⓛⓞⓥⓔ ｡°º¤•εïз ╬㊈㊉㊊㊋㊌㊍㊎㊏ ㊐㊑㊒㊓㊔㊕㊖◊① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ™╬ ღ ♂ ♀ ♥ ↔ ↕ → ← ▪ ๑ ▄ █ ▌ ✄ © ® ⁂ ░ ▒ ▒ ▓ ◊ ◦ ♠ ♣ ♪ の → ° ■ ♀ Ψ № ← ∑ ξ ζ ω ∏ √ ∩ ¤ ∞ ≡ ▄ ≠ ^_^ ─ = » « ﺴ ۩ ๑ ๑ ۩ ۞ ۩ ๑ ▲ γ ō◊♥╠═╝▫■□۩۞๑»«ஐҳ̸Ҳ̸ҳ©†εïз♪ღ♣♠•±җ۝°•ോ ൌ ് ൗ ൠ ാ ി ീ ു ൂ ൃ ಂ ಃ ಅ ಆ ಇ ಈ ಉ ಊ ಋ ಌ ಎ ಏ ಐ ಒ ಓ ಔ ಕ ಖ ಗ ಘ ಙ ಚ ಛ ೠ ೡ ೦ ೧ ೨ ೩ ೪ ೫ ೬ ೭ ೮ ೯ ௩ ௪ ௫ ௬ ௭ ௮ ௯ ௰ ௱ ௲ ભ મ ય ર લ ળ વ શ४ ५ ६ ७ ८ ९॑ ॒ ॓ ॔ क़ ख़ ग़ ज़ ड़ ढ़ फ़ य़ ॠ ॡ ॢ ॣ । ॥ ० १ा ि ी ु ू ृ ँ ं ः ॄ ॅ ॆ े ै ॉ ॊ ो ौ ् ़ॐ २ ڧ ڨ ை३ஹ ஸ ್ರ » ಳ್௮ ಆ ಕ್ಷ್ ఋ ன ಠ್ ಳ್ ப ம உ ஊ ఊ ௌ ொ இ ౖ ௲ ூ ஃ ஊ ஏ ஐ ஒ ஓ ஔ ஜ ஞ ి ಔ ృ ూ ప ௯ ௮ ி ஞ ஜ ಋ ౡౠౖ ಱ ಯ ಮ ಭ ಬ ￼ ҈ لّـّـّّا ® © җ ♥♂ ♀ ♥ ↔ ↕ ▪ ๑ ಕ▄ █ °¹²³∙ ▒ ◊ ◦ ♠ ♣ ♪ の →°■♀ Ψ №← ∑ ξ ζ ω ∏ √ ∩¤ ∞≡ ▄ ≠ ^_^ ─ = ≈≌ ﺴ۩๑ ๑۩۞۩๑ ▓ ▲ γ ō ╦ ╩ ε ┘ ┌ ╬ ω § Θ I ™ ۣ۞ ۝ù ν ώ x ч ž ۩₪۩ﺴ۩๑ ೪.೫ ๑۩۞۩๑ »»–><–«« ๑۩۞۩๑๑۩ﺴ≈۩₪۩ ∂ † ‡ ‼ ﻙ ფ ﻍ ﻪა ბ გ დ ხ ჯ ჰ ჱ ე ป ผ ฝ พ ฟ ภ ม ย ร ฤ ล ฦ ว ศ ษ ส •.:.•ോ سيفભ મ ય ર લ ળ વ શ ષ સ હ ઼ ઽ ા િ ી ુ ૂ ૃ ૄ ૅ ે ૈ ૉ ો ૌ ્ড ঢ ণ ত থ দ ধ ন প ফ ব ভ ম য র ল শ ষ স ঁ ং ঃ অ আ ই ঈ উ ঊ ঋ ঌ এ ঐ ও ঔ ক খ গহಐ ಓ ಔ ಕ ಖ ಗ ಘ ಙ ಝ ಞ ಲ ಶ ಹ ೀ ಾ ಿ ಧಿ ೈ ೋ ೌ ೬ ೂ ೄ.:｡✿*ﾟ‘ﾟ･✿.｡.:* *.:｡✿*ﾟ’ﾟ･✿.｡.:* *.:｡✿*ﾟ¨ﾟ✎･ ✿.｡.:* *.:｡✿*ﾟ¨ﾟ✎･✿.｡.:*【】√ ¤ ∞ ㊝ ≡ ✖ ™ 乀 の♈ ◖◗♋ 灬 ≈ ◈Ш ǎ ☃ ☎ ☏ ☺ ☻ ▧ ▨ ♨ ◐ค ๒ ς ๔ є Ŧ ﻮ ђ เ ן к l ๓ ภ ๏ ק ợ г ร t ย ש ฬ ץ א zα в c ∂ ε ғ g н ι נ к ℓ м η σ ρ q я s т υ v ω x ү zά в ς đ έ ғģ ħ ί ј ķ Ļ м ή ό ρ q ŕ ş ţ ù ν ώ x ч ž"
        k = DebateME().encode_key(mdp)
        pt.key_int_file(k)
        self.assertTrue(pt.check_passwd(mdp))

    def test_valid_key_with_special_car(self):
        pt = Passthrough("./Mount", "clé")
        mdp = "╬╫╪╩╨╧╦╥╤╣╢╡╟╞╝╜╛╙╘╗╖ ╔╔╓╒═┼┴┬├┘└┐│─⌡⌠⌐–—―‗"
        k = DebateME().encode_key(mdp)
        pt.key_int_file(k)
        self.assertTrue(pt.check_passwd(mdp))

    def test_valid_key_with_circled_number(self):
        pt = Passthrough("./Mount", "clé")
        mdp = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳"
        k = DebateME().encode_key(mdp)
        pt.key_int_file(k)
        self.assertTrue(pt.check_passwd(mdp))

    def test_valid_key_with_circled_letters(self):
        pt = Passthrough("./Mount", "clé")
        mdp = "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ"
        k = DebateME().encode_key(mdp)
        pt.key_int_file(k)
        self.assertTrue(pt.check_passwd(mdp))

    def test_valid_key_with_math_symbol(self):
        pt = Passthrough("./Mount", "clé")
        mdp = "%^]-\|®™÷×[]³£ß«»©@{}µ«»±~¡^°`•´˜¨¤! »#$%&/()=?*~{};:_> @1234567890’ ^[]²³y<,.-"
        k = DebateME().encode_key(mdp)
        pt.key_int_file(k)
        self.assertTrue(pt.check_passwd(mdp))

    def test_valid_key_with_asian_car(self):
        pt = Passthrough("./Mount", "clé")
        mdp = "这`~真漂亮`~好温馨敬 語 今 日 ちゃん c は c 漫 画 音 楽 동 방 신 기 今 天 我 就 知 道 自 己 す べ て を 見 失 雪 化 粧 桜 色 舞 う こ ろ －中 島 美 嘉 今 の 気 持 ち 私 の 事 何v聞vいvてvね無 理"
        k = DebateME().encode_key(mdp)
        pt.key_int_file(k)
        self.assertTrue(pt.check_passwd(mdp))

    def test_valid_key_with_arabian(self):
        pt = Passthrough("./Mount", "clé")
        mdp = " ت٤   ئ بت ج خ ذ ز ش ض ظ غ ف ق ك ل ي ٤ שׂ ﮓ ﺼ ﻅ ﻺ ? ﻲ ﻱ ﻒ ﻦ ﺺ ﺵ ﷲ"
        k = DebateME().encode_key(mdp)
        pt.key_int_file(k)
        self.assertTrue(pt.check_passwd(mdp))

    def test_valid_key_with_math_greek(self):
        pt = Passthrough("./Mount", "clé")
        mdp = "α β γ δ ε ζ η θ ι κ λ μ ν ξ ο π ρ σ τ υ φ χ ψ ω"
        k = DebateME().encode_key(mdp)
        pt.key_int_file(k)
        self.assertTrue(pt.check_passwd(mdp))

    def test_valid_key_with_math_special_car(self):
        pt = Passthrough("./Mount", "clé")
        mdp = "♪♀♂ ¤ o▼ ^^ ≡ ☆O Ξ ・ 【寝室】* ω 三 団 θ 皿Θ ε 人 中 朝 ∬ 向 鹵 彡 ۩ ۞ ∞ ∫ ≈ ≠ ≤≥ ▪ ▫ ◊ ● □ † ♥ * ∑ σ エットォ ＾＝ ζ ∂ ☆ •´¯¥¯`• •·.·´¯`·.·• ]¦•¦[ ¤·· § ° –^v^• ζ 食"
        k = DebateME().encode_key(mdp)
        pt.key_int_file(k)
        self.assertTrue(pt.check_passwd(mdp))

    def test_huge_key(self):
        pt = Passthrough("./Mount", "clé")
        mdp = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains."
        k = DebateME().encode_key(mdp)
        pt.key_int_file(k)
        self.assertTrue(pt.check_passwd(mdp))


if __name__ == '__main__':
    unittest.main()

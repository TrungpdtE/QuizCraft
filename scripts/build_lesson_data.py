"""Build curated English lesson files for the learning app."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATABASE = ROOT / "backend" / "database"


WORD_FORM_LESSONS = {
    "01_daily_communication.json": """
giao tiếp|communicate|communicate|communication|communicative|communicatively
giới thiệu|introduce|introduce|introduction|introductory|
mô tả|describe|describe|description|descriptive|descriptively
giải thích|explain|explain|explanation|explanatory|
thảo luận|discuss|discuss|discussion|discussable|
đồng ý|agree|agree|agreement|agreeable|agreeably
không đồng ý|disagree|disagree|disagreement|disagreeable|disagreeably
xin lỗi|apologize|apologize|apology|apologetic|apologetically
mời|invite|invite|invitation|inviting|invitingly
đề nghị|suggest|suggest|suggestion|suggestive|suggestively
quyết định|decide|decide|decision|decisive|decisively
lựa chọn|choose|choose|choice|chosen|
thích hơn|prefer|prefer|preference|preferable|preferably
cần thiết|need|need|necessity|necessary|necessarily
hy vọng|hope|hope|hope|hopeful|hopefully
lo lắng|worry|worry|worry|worried|worryingly
ngạc nhiên|surprise|surprise|surprise|surprising|surprisingly
thoải mái|comfort|comfort|comfort|comfortable|comfortably
khác biệt|differ|differ|difference|different|differently
tương tự|similar||similarity|similar|similarly
thường xuyên|frequent|frequent|frequency|frequent|frequently
hiếm|rare||rarity|rare|rarely
đúng|correct|correct|correction|correct|correctly
sai|mistake|mistake|mistake|mistaken|mistakenly
rõ ràng|clarify|clarify|clarity|clear|clearly
đơn giản|simplify|simplify|simplicity|simple|simply
thật|real||reality|real|really
an toàn|safe|||safe|safely
nguy hiểm|endanger|endanger|danger|dangerous|dangerously
giúp đỡ|help|help|help|helpful|helpfully
""",
    "02_workplace_english.json": """
tổ chức|organize|organize|organization|organizational|organizationally
quản lý|manage|manage|management|managerial|
lập kế hoạch|plan|plan|plan|planned|
chuẩn bị|prepare|prepare|preparation|prepared|
tham gia|participate|participate|participation|participatory|
hợp tác|collaborate|collaborate|collaboration|collaborative|collaboratively
đóng góp|contribute|contribute|contribution|contributory|
hỗ trợ|support|support|support|supportive|supportively
phản hồi|respond|respond|response|responsive|responsively
báo cáo|report|report|report|reportable|
trình bày|present|present|presentation|presentable|
đàm phán|negotiate|negotiate|negotiation|negotiable|
ưu tiên|prioritize|prioritize|priority|prioritized|
lên lịch|schedule|schedule|schedule|scheduled|
hoàn thành|complete|complete|completion|complete|completely
tiếp tục|continue|continue|continuation|continuous|continuously
tiến bộ|progress|progress|progress|progressive|progressively
thành công|succeed|succeed|success|successful|successfully
thất bại|fail|fail|failure|failed|
cải thiện|improve|improve|improvement|improved|
phát triển|develop|develop|development|developmental|
đánh giá|evaluate|evaluate|evaluation|evaluative|
đo lường|measure|measure|measurement|measurable|measurably
chịu trách nhiệm|responsible||responsibility|responsible|responsibly
chuyên nghiệp|professional||profession|professional|professionally
hiệu quả|effective||effectiveness|effective|effectively
hiệu suất|perform|perform|performance|performant|
năng suất|produce|produce|productivity|productive|productively
linh hoạt|adapt|adapt|adaptability|adaptable|adaptably
đáng tin cậy|rely|rely|reliability|reliable|reliably
""",
    "03_intern_interview.json": """
ứng tuyển|apply|apply|application|applicable|
đủ điều kiện|qualify|qualify|qualification|qualified|
có kinh nghiệm|experience|experience|experience|experienced|
giáo dục|educate|educate|education|educational|educationally
đào tạo|train|train|training|trained|
học|learn|learn|learning|learned|
hiểu|understand|understand|understanding|understandable|understandably
biết|know|know|knowledge|knowledgeable|knowledgeably
giải quyết|solve|solve|solution|solvable|
phân tích|analyze|analyze|analysis|analytical|analytically
lý luận|reason|reason|reason|reasonable|reasonably
sáng tạo|create|create|creation|creative|creatively
tò mò|inquire|inquire|inquiry|inquisitive|inquisitively
tự tin|confide|confide|confidence|confident|confidently
trung thực|honor|honor|honesty|honest|honestly
độc lập|independent||independence|independent|independently
chủ động|proactive||initiative|proactive|proactively
kiên nhẫn|patient||patience|patient|patiently
cẩn thận|care|care|care|careful|carefully
chính xác|accurate||accuracy|accurate|accurately
cam kết|commit|commit|commitment|committed|
thích nghi|adapt|adapt|adaptation|adaptive|adaptively
thử thách|challenge|challenge|challenge|challenging|
đạt được|achieve|achieve|achievement|achievable|
chứng minh|demonstrate|demonstrate|demonstration|demonstrable|demonstrably
thuyết phục|persuade|persuade|persuasion|persuasive|persuasively
lãnh đạo|lead|lead|leadership|leading|
giao nhiệm vụ|assign|assign|assignment|assigned|
mong đợi|expect|expect|expectation|expected|expectedly
phù hợp|suit|suit|suitability|suitable|suitably
""",
    "04_backend_engineering.json": """
lập trình|program|program|program|programmable|programmatically
phát triển|develop|develop|development|developmental|
triển khai|deploy|deploy|deployment|deployable|
cấu hình|configure|configure|configuration|configurable|
xác thực danh tính|authenticate|authenticate|authentication|authenticated|
phân quyền|authorize|authorize|authorization|authorized|
xác nhận hợp lệ|validate|validate|validation|valid|validly
mã hóa|encrypt|encrypt|encryption|encrypted|
giải mã|decrypt|decrypt|decryption|decrypted|
lưu trữ tạm|cache|cache|cache|cacheable|
truy vấn|query|query|query|queryable|
lập chỉ mục|index|index|index|indexed|
di chuyển dữ liệu|migrate|migrate|migration|migratory|
tích hợp|integrate|integrate|integration|integrated|
phụ thuộc|depend|depend|dependency|dependent|dependently
đồng thời|concur|concur|concurrency|concurrent|concurrently
bất đồng bộ|synchronize|synchronize|asynchrony|asynchronous|asynchronously
mở rộng|scale|scale|scalability|scalable|
sẵn sàng|available||availability|available|readily
nhất quán|consist|consist|consistency|consistent|consistently
bền vững|persist|persist|persistence|persistent|persistently
phục hồi|recover|recover|recovery|recoverable|
dự phòng|replicate|replicate|replication|replicable|
giám sát|monitor|monitor|monitoring|monitored|
ghi nhật ký|log|log|log|logged|
gỡ lỗi|debug|debug|debugging|debuggable|
kiểm thử|test|test|test|testable|
bảo trì|maintain|maintain|maintenance|maintainable|
tối ưu|optimize|optimize|optimization|optimal|optimally
phản hồi|respond|respond|response|responsive|responsively
""",
    "05_api_database_systems.json": """
kết nối|connect|connect|connection|connected|
ngắt kết nối|disconnect|disconnect|disconnection|disconnected|
gửi|transmit|transmit|transmission|transmissible|
nhận|receive|receive|receipt|receptive|receptively
yêu cầu|request|request|request|requested|
phản hồi|respond|respond|response|responsive|responsively
định tuyến|route|route|route|routable|
phân trang|paginate|paginate|pagination|paginated|
lọc|filter|filter|filter|filterable|
sắp xếp|sort|sort|sort|sortable|
tuần tự hóa|serialize|serialize|serialization|serializable|
chuẩn hóa|normalize|normalize|normalization|normalized|
phi chuẩn hóa|denormalize|denormalize|denormalization|denormalized|
giao dịch|transact|transact|transaction|transactional|transactionally
cam kết dữ liệu|commit|commit|commitment|committed|
khôi phục giao dịch|roll back|roll back|rollback||
khóa|lock|lock|lock|locked|
giới hạn|limit|limit|limitation|limited|
phân phối|distribute|distribute|distribution|distributed|
cân bằng|balance|balance|balance|balanced|
phân vùng|partition|partition|partition|partitioned|
sao chép|replicate|replicate|replication|replicated|
tương thích|compatible||compatibility|compatible|compatibly
không tương thích|incompatible||incompatibility|incompatible|incompatibly
khả dụng|use|use|usability|usable|usably
truy cập|access|access|access|accessible|accessibly
bảo vệ|protect|protect|protection|protective|protectively
tiêu thụ|consume|consume|consumption|consumable|
cung cấp|provide|provide|provision|provided|
đăng ký|subscribe|subscribe|subscription|subscribed|
""",
    "06_ai_engineering.json": """
thông minh|intelligent||intelligence|intelligent|intelligently
học|learn|learn|learning|learned|
huấn luyện|train|train|training|trained|
dự đoán|predict|predict|prediction|predictive|predictively
phân loại|classify|classify|classification|classifiable|
phát hiện|detect|detect|detection|detectable|
nhận diện|recognize|recognize|recognition|recognizable|recognizably
tạo sinh|generate|generate|generation|generative|generatively
nhúng|embed|embed|embedding|embedded|
truy xuất|retrieve|retrieve|retrieval|retrievable|
xếp hạng|rank|rank|ranking|ranked|
đánh giá|evaluate|evaluate|evaluation|evaluative|
tinh chỉnh|fine-tune|fine-tune|fine-tuning|fine-tuned|
suy luận|infer|infer|inference|inferential|inferentially
khái quát hóa|generalize|generalize|generalization|generalizable|
chuyên biệt hóa|specialize|specialize|specialization|specialized|
tối ưu|optimize|optimize|optimization|optimal|optimally
hội tụ|converge|converge|convergence|convergent|
phân kỳ|diverge|diverge|divergence|divergent|divergently
thiên lệch|bias|bias|bias|biased|
 công bằng|fair||fairness|fair|fairly
giải thích được|interpret|interpret|interpretation|interpretable|
minh bạch|transparent||transparency|transparent|transparently
liên quan|relevant||relevance|relevant|relevantly
tương đồng|similar||similarity|similar|similarly
chính xác|precise||precision|precise|precisely
nhớ lại|recall|recall|recall||
ảo giác|hallucinate|hallucinate|hallucination|hallucinatory|
điều phối|orchestrate|orchestrate|orchestration|orchestrated|
tự động hóa|automate|automate|automation|automatic|automatically
""",
}


WORD_TYPE_LESSONS = {
    "01_grammar_foundation.json": """
I am a backend engineering student.|I/PRON am/V a/AR backend/ADJ engineering/N student/N
She writes clean code every day.|She/PRON writes/V clean/ADJ code/N every/DET day/N
The server is currently available.|The/AR server/N is/V currently/ADV available/ADJ
These APIs return structured responses.|These/DET APIs/N return/V structured/ADJ responses/N
We carefully review each assignment.|We/PRON carefully/ADV review/V each/DET assignment/N
An experienced engineer explained the issue.|An/AR experienced/ADJ engineer/N explained/V the/AR issue/N
My application runs smoothly on Linux.|My/DET application/N runs/V smoothly/ADV on/P Linux/N
The new feature looks extremely useful.|The/AR new/ADJ feature/N looks/V extremely/ADV useful/ADJ
They solved the difficult problem quickly.|They/PRON solved/V the/AR difficult/ADJ problem/N quickly/ADV
Our team needs a reliable database.|Our/DET team/N needs/V a/AR reliable/ADJ database/N
He tested the endpoint before deployment.|He/PRON tested/V the/AR endpoint/N before/P deployment/N
This simple script processes files automatically.|This/DET simple/ADJ script/N processes/V files/N automatically/ADV
Users can access the service securely.|Users/N can/V access/V the/AR service/N securely/ADV
The client sent another request.|The/AR client/N sent/V another/DET request/N
Some queries consume excessive memory.|Some/DET queries/N consume/V excessive/ADJ memory/N
Python supports modern asynchronous programming.|Python/N supports/V modern/ADJ asynchronous/ADJ programming/N
The worker completed its task successfully.|The/AR worker/N completed/V its/DET task/N successfully/ADV
We found several critical bugs.|We/PRON found/V several/DET critical/ADJ bugs/N
Each container has an isolated environment.|Each/DET container/N has/V an/AR isolated/ADJ environment/N
Good documentation helps new developers.|Good/ADJ documentation/N helps/V new/ADJ developers/N
""",
    "02_daily_communication.json": """
I usually drink coffee in the morning.|I/PRON usually/ADV drink/V coffee/N in/P the/AR morning/N
Could you speak more slowly please.|Could/V you/PRON speak/V more/ADV slowly/ADV please/ADV
She kindly showed me the nearest station.|She/PRON kindly/ADV showed/V me/PRON the/AR nearest/ADJ station/N
We are meeting our friends after work.|We/PRON are/V meeting/V our/DET friends/N after/P work/N
This restaurant serves delicious local food.|This/DET restaurant/N serves/V delicious/ADJ local/ADJ food/N
I really appreciate your helpful advice.|I/PRON really/ADV appreciate/V your/DET helpful/ADJ advice/N
They arrived late because the bus stopped.|They/PRON arrived/V late/ADV because/CONJ the/AR bus/N stopped/V
Please send me the correct address.|Please/ADV send/V me/PRON the/AR correct/ADJ address/N
My younger brother studies English online.|My/DET younger/ADJ brother/N studies/V English/N online/ADV
We should discuss this matter privately.|We/PRON should/V discuss/V this/DET matter/N privately/ADV
The weather became surprisingly cold today.|The/AR weather/N became/V surprisingly/ADV cold/ADJ today/ADV
I bought these fresh vegetables yesterday.|I/PRON bought/V these/DET fresh/ADJ vegetables/N yesterday/ADV
Can we choose a quieter place.|Can/V we/PRON choose/V a/AR quieter/ADJ place/N
He politely refused their invitation.|He/PRON politely/ADV refused/V their/DET invitation/N
Her explanation was clear and concise.|Her/DET explanation/N was/V clear/ADJ and/CONJ concise/ADJ
The movie was interesting but rather long.|The/AR movie/N was/V interesting/ADJ but/CONJ rather/ADV long/ADJ
Everyone enjoyed the wonderful evening.|Everyone/PRON enjoyed/V the/AR wonderful/ADJ evening/N
I will probably call you later.|I/PRON will/V probably/ADV call/V you/PRON later/ADV
We need enough time for preparation.|We/PRON need/V enough/DET time/N for/P preparation/N
She always answers difficult questions calmly.|She/PRON always/ADV answers/V difficult/ADJ questions/N calmly/ADV
""",
    "03_workplace_interview.json": """
I am applying for the backend internship.|I/PRON am/V applying/V for/P the/AR backend/ADJ internship/N
My recent project demonstrates practical experience.|My/DET recent/ADJ project/N demonstrates/V practical/ADJ experience/N
We collaborated closely with another team.|We/PRON collaborated/V closely/ADV with/P another/DET team/N
I independently designed and implemented the feature.|I/PRON independently/ADV designed/V and/CONJ implemented/V the/AR feature/N
The interviewer asked several technical questions.|The/AR interviewer/N asked/V several/DET technical/ADJ questions/N
Please describe your biggest engineering challenge.|Please/ADV describe/V your/DET biggest/ADJ engineering/N challenge/N
I carefully analyze problems before writing code.|I/PRON carefully/ADV analyze/V problems/N before/P writing/V code/N
Our group successfully delivered the final product.|Our/DET group/N successfully/ADV delivered/V the/AR final/ADJ product/N
This internship offers valuable learning opportunities.|This/DET internship/N offers/V valuable/ADJ learning/N opportunities/N
I can communicate complex ideas clearly.|I/PRON can/V communicate/V complex/ADJ ideas/N clearly/ADV
The manager provided constructive feedback.|The/AR manager/N provided/V constructive/ADJ feedback/N
We frequently organized short planning meetings.|We/PRON frequently/ADV organized/V short/ADJ planning/N meetings/N
My strongest skill is systematic problem solving.|My/DET strongest/ADJ skill/N is/V systematic/ADJ problem/N solving/N
I made a mistake but fixed it quickly.|I/PRON made/V a/AR mistake/N but/CONJ fixed/V it/PRON quickly/ADV
Good interns ask relevant questions proactively.|Good/ADJ interns/N ask/V relevant/ADJ questions/N proactively/ADV
The company expects responsible professional behavior.|The/AR company/N expects/V responsible/ADJ professional/ADJ behavior/N
I want to develop stronger technical skills.|I/PRON want/V to/P develop/V stronger/ADJ technical/ADJ skills/N
We prioritized urgent tasks during the sprint.|We/PRON prioritized/V urgent/ADJ tasks/N during/P the/AR sprint/N
She confidently presented her design decision.|She/PRON confidently/ADV presented/V her/DET design/N decision/N
Learning from failure makes engineers more adaptable.|Learning/N from/P failure/N makes/V engineers/N more/ADV adaptable/ADJ
""",
    "04_backend_api_database.json": """
The API validates every incoming request.|The/AR API/N validates/V every/DET incoming/ADJ request/N
Our middleware handles authentication globally.|Our/DET middleware/N handles/V authentication/N globally/ADV
The database stores user information securely.|The/AR database/N stores/V user/N information/N securely/ADV
This endpoint returns a paginated response.|This/DET endpoint/N returns/V a/AR paginated/ADJ response/N
We added an index to improve performance.|We/PRON added/V an/AR index/N to/P improve/V performance/N
Concurrent transactions may cause unexpected conflicts.|Concurrent/ADJ transactions/N may/V cause/V unexpected/ADJ conflicts/N
The application caches frequently requested data.|The/AR application/N caches/V frequently/ADV requested/ADJ data/N
Each service exposes a stable interface.|Each/DET service/N exposes/V a/AR stable/ADJ interface/N
The worker processes background jobs asynchronously.|The/AR worker/N processes/V background/N jobs/N asynchronously/ADV
Our load balancer distributes traffic evenly.|Our/DET load/N balancer/N distributes/V traffic/N evenly/ADV
Database migrations should be reversible.|Database/N migrations/N should/V be/V reversible/ADJ
The framework automatically serializes Python objects.|The/AR framework/N automatically/ADV serializes/V Python/N objects/N
We use environment variables for sensitive configuration.|We/PRON use/V environment/N variables/N for/P sensitive/ADJ configuration/N
The server logged the failure with useful context.|The/AR server/N logged/V the/AR failure/N with/P useful/ADJ context/N
A retry policy handles temporary network errors.|A/AR retry/N policy/N handles/V temporary/ADJ network/N errors/N
The repository separates business logic from routing.|The/AR repository/N separates/V business/N logic/N from/P routing/N
Integration tests verify complete request flows.|Integration/N tests/N verify/V complete/ADJ request/N flows/N
The deployment pipeline runs all tests automatically.|The/AR deployment/N pipeline/N runs/V all/DET tests/N automatically/ADV
Proper monitoring detects performance degradation early.|Proper/ADJ monitoring/N detects/V performance/N degradation/N early/ADV
Horizontal scaling increases overall system capacity.|Horizontal/ADJ scaling/N increases/V overall/ADJ system/N capacity/N
""",
    "05_system_design_security.json": """
A distributed system contains multiple independent nodes.|A/AR distributed/ADJ system/N contains/V multiple/ADJ independent/ADJ nodes/N
Strong consistency usually increases coordination cost.|Strong/ADJ consistency/N usually/ADV increases/V coordination/N cost/N
The queue temporarily stores unprocessed messages.|The/AR queue/N temporarily/ADV stores/V unprocessed/ADJ messages/N
Consumers read events from separate partitions.|Consumers/N read/V events/N from/P separate/ADJ partitions/N
Replication improves availability during hardware failures.|Replication/N improves/V availability/N during/P hardware/N failures/N
Rate limiting protects public endpoints from abuse.|Rate/N limiting/N protects/V public/ADJ endpoints/N from/P abuse/N
The gateway routes external traffic to internal services.|The/AR gateway/N routes/V external/ADJ traffic/N to/P internal/ADJ services/N
Encrypted connections prevent accidental data exposure.|Encrypted/ADJ connections/N prevent/V accidental/ADJ data/N exposure/N
Authorization determines which resources users can access.|Authorization/N determines/V which/DET resources/N users/N can/V access/V
We never store plain passwords directly.|We/PRON never/ADV store/V plain/ADJ passwords/N directly/ADV
Idempotent operations safely support repeated requests.|Idempotent/ADJ operations/N safely/ADV support/V repeated/ADJ requests/N
Eventual consistency allows temporary differences between replicas.|Eventual/ADJ consistency/N allows/V temporary/ADJ differences/N between/P replicas/N
A circuit breaker prevents cascading failures.|A/AR circuit/N breaker/N prevents/V cascading/ADJ failures/N
Health checks continuously monitor service availability.|Health/N checks/N continuously/ADV monitor/V service/N availability/N
Backups enable recovery after serious incidents.|Backups/N enable/V recovery/N after/P serious/ADJ incidents/N
Observability combines logs metrics and traces.|Observability/N combines/V logs/N metrics/N and/CONJ traces/N
The cache reduces repeated database queries significantly.|The/AR cache/N reduces/V repeated/ADJ database/N queries/N significantly/ADV
Message brokers decouple producers from consumers.|Message/N brokers/N decouple/V producers/N from/P consumers/N
Secure systems follow the least privilege principle.|Secure/ADJ systems/N follow/V the/AR least/ADJ privilege/N principle/N
Regular audits identify hidden security risks.|Regular/ADJ audits/N identify/V hidden/ADJ security/N risks/N
""",
    "06_ai_ml_llm.json": """
Machine learning models discover patterns from data.|Machine/N learning/N models/N discover/V patterns/N from/P data/N
The training process gradually minimizes prediction error.|The/AR training/N process/N gradually/ADV minimizes/V prediction/N error/N
Neural networks contain many adjustable parameters.|Neural/ADJ networks/N contain/V many/DET adjustable/ADJ parameters/N
This classifier predicts the correct category accurately.|This/DET classifier/N predicts/V the/AR correct/ADJ category/N accurately/ADV
We evaluate model performance on unseen examples.|We/PRON evaluate/V model/N performance/N on/P unseen/ADJ examples/N
Overfitting causes poor generalization to new data.|Overfitting/N causes/V poor/ADJ generalization/N to/P new/ADJ data/N
Data preprocessing removes noisy or invalid samples.|Data/N preprocessing/N removes/V noisy/ADJ or/CONJ invalid/ADJ samples/N
The embedding model represents text as dense vectors.|The/AR embedding/N model/N represents/V text/N as/P dense/ADJ vectors/N
Vector databases retrieve semantically similar documents.|Vector/N databases/N retrieve/V semantically/ADV similar/ADJ documents/N
The reranker selects more relevant search results.|The/AR reranker/N selects/V more/ADV relevant/ADJ search/N results/N
Retrieval augmented generation reduces factual hallucinations.|Retrieval/N augmented/ADJ generation/N reduces/V factual/ADJ hallucinations/N
Large language models generate contextually appropriate responses.|Large/ADJ language/N models/N generate/V contextually/ADV appropriate/ADJ responses/N
Prompt engineering guides model behavior effectively.|Prompt/N engineering/N guides/V model/N behavior/N effectively/ADV
Fine tuning adapts a general model to specialized tasks.|Fine/ADJ tuning/N adapts/V a/AR general/ADJ model/N to/P specialized/ADJ tasks/N
Quantization significantly reduces model memory usage.|Quantization/N significantly/ADV reduces/V model/N memory/N usage/N
Batch inference processes multiple inputs simultaneously.|Batch/N inference/N processes/V multiple/ADJ inputs/N simultaneously/ADV
The agent autonomously chooses appropriate tools.|The/AR agent/N autonomously/ADV chooses/V appropriate/ADJ tools/N
Human feedback improves response quality and safety.|Human/ADJ feedback/N improves/V response/N quality/N and/CONJ safety/N
Bias evaluation reveals unfair model behavior.|Bias/N evaluation/N reveals/V unfair/ADJ model/N behavior/N
Production monitoring detects model drift early.|Production/N monitoring/N detects/V model/N drift/N early/ADV
""",
}


def parse_word_forms(raw: str) -> list[dict]:
    items = []
    keys = ("verb", "noun", "adjective", "adverb")
    for line in clean_lines(raw):
        vietnamese, english, *values = line.split("|")
        forms = {key: value for key, value in zip(keys, values) if value}
        items.append({"vietnamese": vietnamese, "english": english, "forms": forms})
    return items


def parse_word_types(raw: str) -> list[dict]:
    items = []
    for line in clean_lines(raw):
        sentence, encoded_tokens = line.split("|", 1)
        tokens = []
        for encoded in encoded_tokens.split():
            word, word_type = encoded.rsplit("/", 1)
            tokens.append({"word": word, "type": word_type})
        items.append({"sentence": sentence, "tokens": tokens})
    return items


def clean_lines(raw: str) -> list[str]:
    return [line.strip() for line in raw.strip().splitlines() if line.strip()]


def write_lessons(folder: str, lessons: dict[str, str], parser) -> None:
    destination = DATABASE / folder
    destination.mkdir(parents=True, exist_ok=True)
    for filename, raw in lessons.items():
        data = parser(raw)
        (destination / filename).write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"{folder}/{filename}: {len(data)} items")


if __name__ == "__main__":
    write_lessons("word_forms", WORD_FORM_LESSONS, parse_word_forms)
    write_lessons("word_types", WORD_TYPE_LESSONS, parse_word_types)

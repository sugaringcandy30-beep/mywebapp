import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="메이플 비치 자산관리 RPG", page_icon="🍁", layout="wide")

st.title("🏙️ 모던 벡터 시티 & 투자 RPG")
st.caption("방향키(A, D)로 이동, Space키로 점프! 주식 매수/매도 시 잔고와 매수가능 수량이 즉시 실시간 반영됩니다.")

game_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    @import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;700&display=swap');

    body {
        margin: 0;
        padding: 0;
        background-color: #0b0f19;
        color: #f8fafc;
        font-family: 'Pretendard', sans-serif;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    #newsTickerBox {
        width: 840px;
        background: rgba(30, 41, 59, 0.75);
        backdrop-filter: blur(10px);
        color: #38bdf8;
        font-size: 14px;
        font-weight: 600;
        padding: 10px 18px;
        border-radius: 16px 16px 0 0;
        border: 1px solid rgba(56, 189, 248, 0.3);
        border-bottom: none;
        box-sizing: border-box;
        display: flex;
        align-items: center;
        gap: 12px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }
    #newsTag {
        background: linear-gradient(135deg, #f43f5e, #e11d48);
        color: white;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    #newsText {
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    #gameContainer {
        position: relative;
    }
    canvas {
        border: 1px solid rgba(56, 189, 248, 0.3);
        border-radius: 0 0 16px 16px;
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
        box-shadow: 0 20px 40px rgba(0,0,0,0.6);
        outline: none;
    }
    #uiBox {
        width: 840px;
        background: rgba(15, 23, 42, 0.85);
        backdrop-filter: blur(12px);
        padding: 16px 20px;
        border-radius: 16px;
        margin-top: 12px;
        box-sizing: border-box;
        border: 1px solid rgba(56, 189, 248, 0.25);
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .status-bar {
        display: flex;
        justify-content: space-between;
        margin-bottom: 10px;
        font-weight: 600;
        color: #e2e8f0;
        font-size: 14px;
    }
    #progressContainer {
        width: 100%;
        height: 20px;
        background: rgba(30, 41, 59, 0.8);
        border-radius: 10px;
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(56, 189, 248, 0.2);
        margin-bottom: 10px;
    }
    #progressBar {
        width: 1%;
        height: 100%;
        background: linear-gradient(90deg, #3b82f6, #10b981);
        transition: width 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        border-radius: 10px;
    }
    #progressText {
        position: absolute;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        font-size: 11px;
        text-align: center;
        line-height: 20px;
        color: white;
        font-weight: 600;
        text-shadow: 0 1px 2px rgba(0,0,0,0.6);
    }
    .action-btn {
        background: linear-gradient(135deg, #3b82f6, #1d4ed8);
        color: white;
        border: none;
        padding: 6px 12px;
        margin: 2px;
        border-radius: 8px;
        cursor: pointer;
        font-family: 'Pretendard', sans-serif;
        font-size: 13px;
        font-weight: 600;
        box-shadow: 0 2px 8px rgba(59, 130, 246, 0.4);
        transition: all 0.15s ease;
    }
    .action-btn:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.6);
    }
    .sell-btn {
        background: linear-gradient(135deg, #f43f5e, #e11d48);
        color: white;
        border: none;
        padding: 6px 12px;
        margin: 2px;
        border-radius: 8px;
        cursor: pointer;
        font-family: 'Pretendard', sans-serif;
        font-size: 13px;
        font-weight: 600;
        box-shadow: 0 2px 8px rgba(244, 63, 94, 0.4);
    }
    .enter-btn {
        background: linear-gradient(135deg, #10b981, #059669);
        color: white;
        border: none;
        padding: 10px 22px;
        border-radius: 10px;
        cursor: pointer;
        font-family: 'Pretendard', sans-serif;
        font-size: 15px;
        font-weight: 600;
        box-shadow: 0 4px 14px rgba(16, 185, 129, 0.4);
    }
    .exit-btn {
        background: linear-gradient(135deg, #64748b, #475569);
        color: white;
        border: none;
        padding: 8px 16px;
        margin: 4px;
        border-radius: 8px;
        cursor: pointer;
        font-family: 'Pretendard', sans-serif;
        font-size: 13px;
        font-weight: 600;
    }
    .restart-btn {
        background: linear-gradient(135deg, #f59e0b, #d97706);
        color: white;
        border: none;
        padding: 12px 30px;
        border-radius: 10px;
        cursor: pointer;
        font-family: 'Pretendard', sans-serif;
        font-size: 16px;
        font-weight: 700;
        box-shadow: 0 6px 20px rgba(245, 158, 11, 0.5);
        transition: all 0.2s ease;
    }
    .controls {
        display: grid;
        grid-template-columns: repeat(4, 90px);
        gap: 12px;
        justify-content: center;
        margin-top: 14px;
    }
    .ctrl-btn {
        width: 90px;
        height: 50px;
        font-size: 15px;
        font-weight: 600;
        font-family: 'Pretendard', sans-serif;
        background: rgba(30, 41, 59, 0.9);
        color: #38bdf8;
        border: 1px solid rgba(56, 189, 248, 0.3);
        border-radius: 12px;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        transition: all 0.1s ease;
    }
    .ctrl-btn:active {
        transform: translateY(2px);
        background: rgba(56, 189, 248, 0.2);
    }
    #dialogue {
        min-height: 40px;
        background: rgba(15, 23, 42, 0.6);
        padding: 10px 14px;
        border-radius: 10px;
        border: 1px solid rgba(56, 189, 248, 0.15);
        margin-top: 6px;
        font-size: 14px;
        line-height: 1.5;
        color: #cbd5e1;
    }
    .stock-card {
        background: rgba(30, 41, 59, 0.6);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 8px;
        padding: 8px 12px;
        margin-bottom: 6px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .news-item {
        background: rgba(30, 41, 59, 0.5);
        border-left: 3px solid #38bdf8;
        padding: 6px 10px;
        margin-bottom: 6px;
        border-radius: 4px;
        font-size: 12px;
        text-align: left;
        color: #e2e8f0;
    }
</style>
</head>
<body>

<div id="newsTickerBox">
    <span id="newsTag">실시간 속보</span>
    <span id="newsText">모던 벡터 시티 금융 시장이 개장했습니다. 시황을 예의주시하세요.</span>
</div>

<div id="gameContainer">
    <canvas id="gameCanvas" width="840" height="480" tabindex="1"></canvas>
</div>

<div id="uiBox">
    <div class="status-bar">
        <span>📍 위치: <span id="locationText" style="color: #38bdf8;">메인 스트리트</span></span>
        <span>☀️ 시간대: <span id="dayNightText" style="color: #fbbf24;">아침 🌅</span></span>
        <span>📅 턴: <span id="turnText">1</span>/12</span>
        <span>💰 총 자산: <span id="moneyText" style="color: #10b981;">1,000,000</span>원 (현금: <span id="cashText" style="color: #38bdf8;">1,000,000</span>원)</span>
    </div>

    <div id="progressContainer">
        <div id="progressBar"></div>
        <div id="progressText">1억 원 목표 달성도: 1%</div>
    </div>

    <div id="dialogue">💬 방향키로 세련된 벡터 빌딩들을 탐험하고 입구 포탈[▲ / W]로 입장해보세요.</div>
    <div id="actionArea" style="margin-top: 8px; text-align: center;"></div>
</div>

<div class="controls">
    <button class="ctrl-btn" onclick="moveLeft()">◄ 이동</button>
    <button class="ctrl-btn" onclick="jump()">▲ 점프</button>
    <button class="ctrl-btn" onclick="moveRight()">이동 ►</button>
    <button class="ctrl-btn" style="color: #10b981; border-color: rgba(16, 185, 129, 0.4);" onclick="interactPortal()">▲ 포탈</button>
</div>

<script>
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

window.addEventListener('load', () => {
    canvas.focus();
});

let cash = 1000000;
let turn = 1;
let isDay = true;
let currentScene = 'town';
let ownedBuildings = [];
const goalMoney = 100000000;
let isGameOver = false;
let gameResult = ''; 

let stocks = [
    { id: 'neotech', name: '🚀 네오 테크', price: 50000, prevPrice: 50000, owned: 0, totalCost: 0, volatility: 0.35 },
    { id: 'bluechips', name: '🛡️ 블루 칩스', price: 100000, prevPrice: 100000, owned: 0, totalCost: 0, volatility: 0.10 },
    { id: 'cyberenergy', name: '⚡ 사이버 에너지', price: 20000, prevPrice: 20000, owned: 0, totalCost: 0, volatility: 0.22 }
];

let floatingTexts = [];
let newsArchive = [
    "[턴 1] 모던 벡터 시티 금융 시장 정식 개장. 투자자들의 기대감 고조."
];

let currentNews = { text: "모던 벡터 시티 금융 시장 정식 개장. 투자자들의 기대감 고조.", stockMod: 0 };

const newsEvents = [
    { text: "🔥 [특보] 테크 기업 연합 대규모 설비 투자 단행... 시장의 자금이 한 곳으로 몰릴 조짐이 보입니다.", stockMod: 0.28 },
    { text: "📉 [긴급] 글로벌 무역 긴장감 고조 및 리스크 회피 심리 확산... 안전 자산 선호가 대두될 수 있습니다.", stockMod: -0.22 },
    { text: "🚀 [속보] 중앙은행의 전격적인 유동성 확장 정책 시사... 증시에 강력한 순풍이 불어 닥칠 전망입니다.", stockMod: 0.32 },
    { text: "⚠️ [경고] 예상보다 매서운 물가 상승 압력 포착... 투자자들 사이에서 긴축 우려가 조심스럽게 피어오릅니다.", stockMod: -0.18 }
];

const player = {
    x: 120,
    y: 320,
    vx: 0,
    vy: 0,
    speed: 7,
    jumpPower: -13,
    groundY: 320,
    isGrounded: true,
    facing: 'right',
    animFrame: 0,
    name: '투자자'
};

const buildings = [
    { id: 'bank', name: '🏦 네오 중앙은행', x: 120, portalX: 220, colorMain: '#1e293b', accent: '#10b981' },
    { id: 'stock', name: '📈 메트로 증권타워', x: 500, portalX: 600, colorMain: '#1e293b', accent: '#3b82f6' },
    { id: 'crypto', name: '🚀 사이버 코인랩', x: 880, portalX: 980, colorMain: '#1e293b', accent: '#f43f5e' },
    { id: 'realty', name: '🏢 스카이 부동산', x: 1260, portalX: 1360, colorMain: '#1e293b', accent: '#fbbf24' }
];

const interiorNPCs = {
    bank: { x: 420, y: 290, name: '🏦 은행 딜러 김수호' },
    stock: { x: 420, y: 290, name: '📈 펀드매니저 박차트' },
    crypto: { x: 420, y: 290, name: '🚀 코인 애널리스트 나대박' },
    realty: { x: 420, y: 290, name: '🏢 부동산 디벨로퍼 최건물' }
};

let cameraX = 0;
let portalAnim = 0;
let keys = {};
let lastProximityKey = null;

document.addEventListener('keydown', (e) => {
    if (isGameOver) return;
    if(["Space","ArrowUp","ArrowDown","ArrowLeft","ArrowRight"].indexOf(e.code) > -1) {
        e.preventDefault();
    }
    keys[e.key] = true;
    if ((e.key === 'ArrowUp' || e.key === 'w' || e.key === 'W') && currentScene === 'town') {
        interactPortal();
    }
    if ((e.key === ' ' || e.key === 'Spacebar') && player.isGrounded) {
        jump();
    }
});
document.addEventListener('keyup', (e) => { keys[e.key] = false; });

function moveLeft() { if (!isGameOver) { player.vx = -player.speed; player.facing = 'left'; } }
function moveRight() { if (!isGameOver) { player.vx = player.speed; player.facing = 'right'; } }
function jump() {
    if (!isGameOver && player.isGrounded) {
        player.vy = player.jumpPower;
        player.isGrounded = false;
    }
}

function getTotalAssets() {
    let stockValue = stocks.reduce((sum, s) => sum + (s.owned * s.price), 0);
    return cash + stockValue;
}

function restartGame() {
    cash = 1000000;
    turn = 1;
    isDay = true;
    currentScene = 'town';
    ownedBuildings = [];
    isGameOver = false;
    gameResult = '';
    floatingTexts = [];
    newsArchive = ["[턴 1] 모던 벡터 시티 금융 시장 정식 개장. 투자자들의 기대감 고조."];
    currentNews = { text: "모던 벡터 시티 금융 시장 정식 개장. 투자자들의 기대감 고조.", stockMod: 0 };
    
    stocks.forEach(s => {
        s.owned = 0;
        s.totalCost = 0;
    });
    stocks[0].price = 50000; stocks[0].prevPrice = 50000;
    stocks[1].price = 100000; stocks[1].prevPrice = 100000;
    stocks[2].price = 20000; stocks[2].prevPrice = 20000;

    player.x = 120;
    player.y = 320;
    document.getElementById('locationText').innerText = '메인 스트리트';
    lastProximityKey = null;
    updateUI();
    checkProximity();
    canvas.focus();
}

function addFloatingText(amount) {
    let text = amount >= 0 ? `+${amount.toLocaleString()}원` : `-${Math.abs(amount).toLocaleString()}원`;
    let color = amount >= 0 ? '#10b981' : '#f43f5e';
    floatingTexts.push({
        x: player.x,
        y: player.y - 60,
        text: text,
        color: color,
        opacity: 1.0,
        vy: -1.5
    });
}

function interactPortal() {
    if (isGameOver || currentScene !== 'town') return;
    for (let b of buildings) {
        if (Math.abs(player.x - b.portalX) < 55) {
            enterBuilding(b.id);
            return;
        }
    }
}

function enterBuilding(bId) {
    if (isGameOver) return;
    currentScene = bId;
    player.x = 120;
    player.y = 320;
    lastProximityKey = null;
    const bObj = buildings.find(b => b.id === bId);
    document.getElementById('locationText').innerText = bObj.name;
    canvas.focus();
    checkProximity();
}

function exitBuilding() {
    if (isGameOver) return;
    let bObj = buildings.find(b => b.id === currentScene);
    currentScene = 'town';
    player.x = bObj.portalX;
    player.y = 320;
    lastProximityKey = null;
    document.getElementById('locationText').innerText = '메인 스트리트';
    canvas.focus();
    checkProximity();
}

function triggerGameOver(result) {
    isGameOver = true;
    gameResult = result;
    const actionArea = document.getElementById('actionArea');
    const dialogue = document.getElementById('dialogue');
    
    if (gameResult === 'win') {
        dialogue.innerHTML = "🎉 <b>축하합니다! 1억 원을 달성하여 강남 건물주가 되었습니다!</b>";
    } else {
        dialogue.innerHTML = "❌ <b>12턴이 모두 종료되었습니다. 목표 금액 미달성으로 패배했습니다!</b>";
    }
    actionArea.innerHTML = `<button class="restart-btn" onclick="restartGame()">🔄 다시하기 (RESTART)</button>`;
}

function checkProximity() {
    const actionArea = document.getElementById('actionArea');
    const dialogue = document.getElementById('dialogue');

    if (isGameOver) {
        triggerGameOver(gameResult);
        return;
    }

    if (currentScene === 'town') {
        let nearB = buildings.find(b => Math.abs(player.x - b.portalX) < 55);
        let stateKey = nearB ? 'town_' + nearB.id : 'town_none';

        if (lastProximityKey !== stateKey) {
            lastProximityKey = stateKey;
            if (nearB) {
                dialogue.innerHTML = `✨ <b>[${nearB.name}] 입구입니다!</b> [▲ / W]키나 아래 버튼으로 입장하세요!`;
                actionArea.innerHTML = `<button class="enter-btn" onclick="enterBuilding('${nearB.id}')">🚪 건물 입장하기</button>`;
            } else {
                dialogue.innerHTML = "💬 방향키로 세련된 벡터 빌딩들을 탐험하고 입구 포탈로 들어가보세요!";
                actionArea.innerHTML = "";
            }
        }
    } else {
        let npc = interiorNPCs[currentScene];
        let dist = Math.abs(player.x - npc.x);
        let zone = player.x < 70 ? 'exit' : (dist < 100 ? 'npc' : 'walk');
        let stateKey = currentScene + '_' + zone;

        if (lastProximityKey !== stateKey) {
            lastProximityKey = stateKey;
            if (zone === 'exit') {
                dialogue.innerHTML = "🚪 메인 스트리트로 나가는 출구입니다.";
                actionArea.innerHTML = `<button class="exit-btn" onclick="exitBuilding()">🚪 밖으로 나가기</button>`;
            } else if (zone === 'npc') {
                dialogue.innerHTML = `💬 <b>${npc.name}</b>: "어서오세요! 원하시는 투자 항목을 선택해 주세요."`;
                renderDialogueOptions(currentScene);
            } else {
                dialogue.innerHTML = `🏢 컨설팅 데스크로 가까이 다가가세요.`;
                actionArea.innerHTML = `<button class="exit-btn" onclick="exitBuilding()">🚪 밖으로 나가기</button>`;
            }
        }
    }
}

function renderDialogueOptions(type) {
    const actionArea = document.getElementById('actionArea');
    if (type === 'bank') {
        actionArea.innerHTML = `<button class="action-btn" onclick="investBank()">🏦 예금 가입 (+5% 확정 수익 & 턴 진행)</button> <button class="exit-btn" onclick="exitBuilding()">🚪 나가기</button>`;
    } else if (type === 'stock') {
        renderStockMarketUI();
    } else if (type === 'crypto') {
        actionArea.innerHTML = `<button class="action-btn" style="background: linear-gradient(135deg, #f43f5e, #e11d48);" onclick="investCrypto()">🚀 코인 고위험 고수익 올인 (+100% ~ -50% & 턴 진행)</button> <button class="exit-btn" onclick="exitBuilding()">🚪 나가기</button>`;
    } else if (type === 'realty') {
        actionArea.innerHTML = `
            <button class="action-btn" onclick="buyBuilding('초역세권 오피스텔', 30000000, 2000000)">🏠 오피스텔 (3천만 / 월세 200만)</button>
            <button class="action-btn" onclick="buyBuilding('테헤란로 빌딩', 60000000, 5000000)">🏢 빌딩 (6천만 / 월세 500만)</button>
            <button class="action-btn" onclick="buyBuilding('강남 타워', 100000000, 12000000)">🏙️ 강남타워 (1억 / 월세 1200만)</button>
            <button class="exit-btn" onclick="exitBuilding()">🚪 나가기</button>
        `;
    }
}

function renderStockMarketUI() {
    const actionArea = document.getElementById('actionArea');
    let html = `<div style="display: flex; gap: 10px; align-items: flex-start;">`;
    
    // 왼쪽: 주식 거래 구역
    html += `<div style="flex: 1.3; max-height: 155px; overflow-y: auto; padding-right: 4px;">`;
    stocks.forEach(s => {
        let diff = s.price - s.prevPrice;
        let rate = (diff / s.prevPrice * 100).toFixed(1);
        let color = diff >= 0 ? '#10b981' : '#f43f5e';
        let sign = diff >= 0 ? '+' : '';
        let avgCost = s.owned > 0 ? Math.floor(s.totalCost / s.owned) : 0;
        let returnRate = s.owned > 0 ? (((s.price - avgCost) / avgCost) * 100).toFixed(1) : '0.0';
        let maxBuyable = Math.floor(cash / s.price);

        html += `
            <div class="stock-card">
                <div style="text-align:left;">
                    <span style="font-weight:700; color:#ffffff; font-size:12px;">${s.name}</span>
                    <span style="font-size:11px; color:${color}; margin-left:4px;">${s.price.toLocaleString()}원 (${sign}${rate}%)</span>
                    <div style="font-size:10px; color:#cbd5e1; margin-top:1px;">보유: ${s.owned}주 | 평단: ${avgCost.toLocaleString()}원 | 수익률: <span style="color:${returnRate >= 0 ? '#10b981':'#f43f5e'}">${returnRate}%</span> | <span style="color:#38bdf8;">매수가능: ${maxBuyable}주</span></div>
                </div>
                <div>
                    <button class="action-btn" style="font-size:11px; padding:4px 8px;" onclick="buyStock('${s.id}', 1)">1주매수</button>
                    <button class="action-btn" style="font-size:11px; padding:4px 8px;" onclick="buyStock('${s.id}', 5)">5주매수</button>
                    <button class="sell-btn" style="font-size:11px; padding:4px 8px;" onclick="sellStock('${s.id}', 1)">1주매도</button>
                    <button class="sell-btn" style="font-size:11px; padding:4px 8px;" onclick="sellStock('${s.id}', 5)">전량매도</button>
                </div>
            </div>
        `;
    });
    html += `</div>`;

    // 오른쪽: 실시간 뉴스 게시판 아카이브 구역
    html += `<div style="flex: 1; background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(56, 189, 248, 0.2); border-radius: 8px; padding: 6px 10px; max-height: 155px; overflow-y: auto;">
        <div style="font-size: 12px; font-weight: 700; color: #38bdf8; margin-bottom: 4px; text-align: left;">📰 실시간 뉴스 속보 게시판</div>
    `;
    newsArchive.slice().reverse().forEach(n => {
        html += `<div class="news-item">${n}</div>`;
    });
    html += `</div>`;

    html += `</div>
        <div style="margin-top: 6px;">
            <button class="enter-btn" style="background: linear-gradient(135deg, #3b82f6, #1d4ed8); padding: 7px 16px; font-size: 13px;" onclick="passTurnByStock()">🌙 턴 마치기 (주식 변동 & 아침/밤 전환)</button>
            <button class="exit-btn" onclick="exitBuilding()">🚪 나가기</button>
        </div>
    `;

    actionArea.innerHTML = html;
}

function buyStock(stockId, qty) {
    if (isGameOver) return;
    let s = stocks.find(item => item.id === stockId);
    let totalCost = s.price * qty;
    if (cash < totalCost) { alert("현금이 부족합니다!"); return; }
    
    cash -= totalCost;
    s.owned += qty;
    s.totalCost += totalCost;
    addFloatingText(-totalCost);
    
    // 매수 즉시 UI 및 자산 즉각 반영
    updateUI();
    renderStockMarketUI();
}

function sellStock(stockId, qty) {
    if (isGameOver) return;
    let s = stocks.find(item => item.id === stockId);
    if (s.owned <= 0) { alert("보유한 주식이 없습니다!"); return; }

    let sellQty = (qty === 5) ? s.owned : Math.min(qty, s.owned);
    let revenue = s.price * sellQty;
    
    let avgCost = s.owned > 0 ? (s.totalCost / s.owned) : 0;
    s.owned -= sellQty;
    s.totalCost -= (avgCost * sellQty);
    if (s.owned <= 0) s.totalCost = 0;

    cash += revenue;
    addFloatingText(revenue);
    
    // 매도 즉시 UI 및 자산 즉각 반영
    updateUI();
    renderStockMarketUI();
}

function passTurnByStock() {
    canvas.focus();
    processTurn();
}

function updateStockPrices() {
    stocks.forEach(s => {
        s.prevPrice = s.price;
        let changePercent = (Math.random() * (s.volatility * 2) - s.volatility) + currentNews.stockMod;
        let newPrice = Math.floor(s.price * (1 + changePercent));
        s.price = Math.max(1000, newPrice);
    });
}

function processTurn() {
    if (isGameOver) return;

    isDay = !isDay;
    document.getElementById('dayNightText').innerText = isDay ? "아침 🌅" : "밤 🌙";
    document.getElementById('dayNightText').style.color = isDay ? "#fbbf24" : "#a855f7";

    updateStockPrices();

    let rentSum = 0;
    ownedBuildings.forEach(b => rentSum += b.rent);
    if (rentSum > 0) {
        cash += rentSum;
        addFloatingText(rentSum);
    }
    
    let currentTotalAssets = getTotalAssets();

    if (currentTotalAssets >= goalMoney) {
        updateUI();
        triggerGameOver('win');
        return;
    }

    turn += 1;
    
    if (turn > 12) {
        turn = 12;
        updateUI();
        triggerGameOver('lose');
        return;
    }
    
    if (Math.random() < 0.8) {
        currentNews = newsEvents[Math.floor(Math.random() * newsEvents.length)];
    } else {
        currentNews = { text: "시티 금융 시장이 특별한 이슈 없이 평온한 흐름을 보이고 있습니다.", stockMod: 0 };
    }
    
    let newsFormatted = `[턴 ${turn}] ${currentNews.text}`;
    newsArchive.push(newsFormatted);
    document.getElementById('newsText').innerText = currentNews.text;

    updateUI();
    lastProximityKey = null;

    if (currentScene === 'stock') {
        renderStockMarketUI();
    } else {
        checkProximity();
    }

    if (currentTotalAssets <= 0) {
        updateUI();
        triggerGameOver('lose');
    }
}

function investBank() {
    if (isGameOver) return;
    let interest = Math.floor(cash * 0.05);
    cash += interest;
    addFloatingText(interest);
    canvas.focus();
    processTurn();
}

function investCrypto() {
    if (isGameOver) return;
    let rate = (Math.random() * 1.5) - 0.5;
    let gainLoss = Math.floor(cash * rate);
    cash += gainLoss;
    addFloatingText(gainLoss);
    canvas.focus();
    processTurn();
}

function buyBuilding(name, price, rent) {
    if (isGameOver) return;
    if (cash < price) { alert("현금이 부족합니다!"); return; }
    cash -= price;
    addFloatingText(-price);
    ownedBuildings.push({ name, rent });
    canvas.focus();
    
    if (getTotalAssets() >= goalMoney) {
        updateUI();
        triggerGameOver('win');
        return;
    }
    updateUI();
}

function updateUI() {
    let totalAssets = getTotalAssets();
    document.getElementById('moneyText').innerText = totalAssets.toLocaleString();
    document.getElementById('cashText').innerText = cash.toLocaleString();
    document.getElementById('turnText').innerText = turn > 12 ? 12 : turn;

    let percent = Math.min(100, Math.max(1, Math.floor((totalAssets / goalMoney) * 100)));
    document.getElementById('progressBar').style.width = percent + '%';
    document.getElementById('progressText').innerText = `1억 원 목표 달성도: ${percent}% (총자산 ${totalAssets.toLocaleString()}원 / 100,000,000원)`;
}

function update() {
    if (!isGameOver) {
        if (keys['ArrowLeft'] || keys['a'] || keys['A']) { player.vx = -player.speed; player.facing = 'left'; }
        else if (keys['ArrowRight'] || keys['d'] || keys['D']) { player.vx = player.speed; player.facing = 'right'; }
        else { player.vx *= 0.6; }

        player.x += player.vx;
        player.vy += 0.65;
        player.y += player.vy;

        if (player.y >= player.groundY) {
            player.y = player.groundY;
            player.vy = 0;
            player.isGrounded = true;
        }

        if (currentScene === 'town') {
            player.x = Math.max(20, Math.min(1580, player.x));
            cameraX = player.x - canvas.width / 2;
            cameraX = Math.max(0, Math.min(1600 - canvas.width, cameraX));
        } else {
            player.x = Math.max(20, Math.min(820, player.x));
            cameraX = 0;
        }

        portalAnim += 0.08;
        player.animFrame += 0.15;

        checkProximity();
    }
    
    draw();
    requestAnimationFrame(update);
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.save();
    ctx.translate(-cameraX, 0);

    if (currentScene === 'town') drawTown();
    else drawInterior();

    drawVectorPlayer(player.x, player.y, player.facing);
    drawFloatingTexts();

    ctx.restore();

    if (isGameOver) {
        ctx.save();
        ctx.fillStyle = 'rgba(0, 0, 0, 0.85)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.textAlign = 'center';
        ctx.shadowColor = '#000';
        ctx.shadowBlur = 20;

        let finalAssets = getTotalAssets();
        if (gameResult === 'win') {
            ctx.fillStyle = '#fbbf24';
            ctx.font = '700 48px Pretendard, sans-serif';
            ctx.fillText('YOU WIN!', canvas.width / 2, canvas.height / 2 - 20);

            ctx.fillStyle = '#ffffff';
            ctx.font = '600 18px Pretendard, sans-serif';
            ctx.fillText('축하합니다! 1억 원을 달성하여 강남 건물주가 되었습니다!', canvas.width / 2, canvas.height / 2 + 30);
        } else {
            ctx.fillStyle = '#f43f5e';
            ctx.font = '700 48px Pretendard, sans-serif';
            ctx.fillText('YOU LOSE', canvas.width / 2, canvas.height / 2 - 20);

            ctx.fillStyle = '#cbd5e1';
            ctx.font = '600 18px Pretendard, sans-serif';
            ctx.fillText('12턴 종료! 목표 금액 미달성 최종 자산: ' + finalAssets.toLocaleString() + '원', canvas.width / 2, canvas.height / 2 + 30);
        }
        ctx.restore();
    }
}

function drawTown() {
    let skyGradient = ctx.createLinearGradient(0, 0, 0, 260);
    if (isDay) {
        skyGradient.addColorStop(0, '#0284c7');
        skyGradient.addColorStop(1, '#38bdf8');
    } else {
        skyGradient.addColorStop(0, '#090d16');
        skyGradient.addColorStop(1, '#1e293b');
    }
    ctx.fillStyle = skyGradient;
    ctx.fillRect(cameraX, 0, canvas.width, 260);

    ctx.save();
    if (isDay) {
        ctx.fillStyle = '#fbbf24';
        ctx.shadowColor = '#fbbf24';
        ctx.shadowBlur = 25;
        ctx.beginPath();
        ctx.arc(cameraX + 700, 60, 26, 0, Math.PI * 2);
        ctx.fill();
    } else {
        ctx.fillStyle = '#fef08a';
        ctx.shadowColor = '#fef08a';
        ctx.shadowBlur = 20;
        ctx.beginPath();
        ctx.arc(cameraX + 700, 60, 22, 0, Math.PI * 2);
        ctx.fill();
    }
    ctx.restore();

    ctx.fillStyle = isDay ? 'rgba(255, 255, 255, 0.2)' : 'rgba(30, 41, 59, 0.4)';
    ctx.fillRect(cameraX + 50, 100, 90, 160);
    ctx.fillRect(cameraX + 300, 70, 110, 190);
    ctx.fillRect(cameraX + 700, 80, 100, 180);
    ctx.fillRect(cameraX + 1100, 50, 130, 210);

    ctx.fillStyle = '#1e293b';
    ctx.fillRect(0, 360, 1600, 120);
    ctx.fillStyle = '#334155';
    ctx.fillRect(0, 360, 1600, 6);

    buildings.forEach(b => {
        ctx.fillStyle = b.colorMain;
        ctx.fillRect(b.x, 110, 200, 250);

        for (let wx = b.x + 20; wx < b.x + 180; wx += 40) {
            for (let wy = 140; wy < 320; wy += 45) {
                ctx.fillStyle = isDay ? 'rgba(255, 255, 255, 0.6)' : 'rgba(56, 189, 248, 0.15)';
                ctx.fillRect(wx, wy, 22, 28);
                ctx.fillStyle = 'rgba(251, 191, 36, 0.8)';
                ctx.fillRect(wx + 4, wy + 4, 14, 20);
            }
        }

        ctx.fillStyle = b.accent;
        ctx.fillRect(b.x, 80, 200, 32);
        ctx.fillStyle = '#ffffff';
        ctx.font = '600 15px Pretendard, sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(b.name, b.x + 100, 101);

        let px = b.portalX;
        let py = 320;
        let scale = Math.sin(portalAnim) * 6;
        
        ctx.save();
        ctx.strokeStyle = b.accent;
        ctx.lineWidth = 4;
        ctx.shadowColor = b.accent;
        ctx.shadowBlur = 15;
        ctx.beginPath();
        ctx.ellipse(px, py, 22 + scale, 40 + scale, 0, 0, Math.PI * 2);
        ctx.stroke();
        ctx.fillStyle = b.accent;
        ctx.globalAlpha = 0.25;
        ctx.fill();
        ctx.restore();
    });
}

function drawInterior() {
    let bObj = buildings.find(b => b.id === currentScene);
    let npc = interiorNPCs[currentScene];

    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, 840, 480);
    
    ctx.fillStyle = '#1e293b';
    ctx.fillRect(0, 0, 840, 90);

    ctx.fillStyle = '#1e293b';
    ctx.fillRect(0, 360, 840, 120);

    ctx.fillStyle = '#334155';
    ctx.fillRect(340, 300, 160, 60);
    ctx.fillStyle = '#38bdf8';
    ctx.fillRect(340, 350, 160, 10);

    ctx.save();
    ctx.strokeStyle = '#f43f5e';
    ctx.lineWidth = 4;
    ctx.shadowColor = '#f43f5e';
    ctx.shadowBlur = 15;
    ctx.beginPath();
    ctx.ellipse(40, 320, 18, 36, 0, 0, Math.PI * 2);
    ctx.stroke();
    ctx.restore();

    drawVectorNPC(npc.x, npc.y, npc.name);
}

function drawVectorPlayer(x, y, facing) {
    let bounce = Math.sin(player.animFrame) * 2;
    if (!player.isGrounded) bounce = -6;
    let totalAssets = getTotalAssets();

    if (isGameOver && gameResult === 'lose') {
        ctx.fillStyle = '#475569';
        ctx.beginPath();
        ctx.roundRect(x - 16, y - 38 + bounce, 32, 44, [6]);
        ctx.fill();

        ctx.fillStyle = '#94a3b8';
        ctx.beginPath();
        ctx.roundRect(x - 10, y - 28 + bounce, 20, 14, [4]);
        ctx.fill();

        ctx.fillStyle = '#ef4444';
        ctx.fillRect(x - 4, y - 24 + bounce, 2, 6);
        ctx.fillRect(x + 2, y - 24 + bounce, 2, 6);

        ctx.fillStyle = 'rgba(15, 23, 42, 0.85)';
        ctx.beginPath();
        ctx.roundRect(x - 50, y - 56, 100, 18, [4]);
        ctx.fill();
        ctx.fillStyle = '#f43f5e';
        ctx.font = '600 11px Pretendard, sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('빈털터리 파산자', x, y - 43);
        return;
    }

    if (totalAssets >= 50000000) {
        ctx.save();
        ctx.strokeStyle = '#fbbf24';
        ctx.lineWidth = 3;
        ctx.shadowColor = '#fbbf24';
        ctx.shadowBlur = 18;
        ctx.beginPath();
        ctx.arc(x, y - 18 + bounce, 32, 0, Math.PI * 2);
        ctx.stroke();
        ctx.restore();
    }

    ctx.fillStyle = '#0f172a';
    ctx.beginPath();
    ctx.roundRect(x - 14, y - 42 + bounce, 28, 48, [10]);
    ctx.fill();

    ctx.fillStyle = '#fce7f3';
    ctx.beginPath();
    ctx.roundRect(x - 10, y - 30, 20, 16, [6]);
    ctx.fill();

    if (totalAssets >= 50000000) {
        ctx.fillStyle = '#fbbf24';
        ctx.fillRect(x - 12, y - 38 + bounce, 24, 10);
        ctx.fillStyle = '#fbbf24';
        ctx.fillRect(x - 2, y - 14 + bounce, 4, 16);
    } else if (totalAssets >= 20000000) {
        ctx.fillStyle = '#a855f7';
        ctx.fillRect(x - 12, y - 38 + bounce, 24, 10);
        ctx.fillStyle = '#e2e8f0';
        ctx.fillRect(x - 2, y - 14 + bounce, 4, 16);
    } else {
        ctx.fillStyle = '#3b82f6';
        ctx.fillRect(x - 12, y - 38 + bounce, 24, 10);
        ctx.fillStyle = '#38bdf8';
        if (facing === 'right') {
            ctx.fillRect(x + 2, y - 14 + bounce, 6, 16);
        } else {
            ctx.fillRect(x - 8, y - 14 + bounce, 6, 16);
        }
    }

    ctx.fillStyle = 'rgba(15, 23, 42, 0.85)';
    ctx.beginPath();
    ctx.roundRect(x - 45, y - 62 + bounce, 90, 20, [6]);
    ctx.fill();
    ctx.strokeStyle = 'rgba(56, 189, 248, 0.3)';
    ctx.stroke();

    ctx.fillStyle = totalAssets >= 50000000 ? '#fbbf24' : '#38bdf8';
    ctx.font = '600 12px Pretendard, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText(player.name, x, y - 48 + bounce);
}

function drawFloatingTexts() {
    for (let i = floatingTexts.length - 1; i >= 0; i--) {
        let ft = floatingTexts[i];
        ft.y += ft.vy;
        ft.opacity -= 0.02;

        if (ft.opacity <= 0) {
            floatingTexts.splice(i, 1);
            continue;
        }

        ctx.save();
        ctx.globalAlpha = Math.max(0, ft.opacity);
        ctx.fillStyle = ft.color;
        ctx.font = '700 16px Pretendard, sans-serif';
        ctx.textAlign = 'center';
        ctx.shadowColor = '#000000';
        ctx.shadowBlur = 6;
        ctx.fillText(ft.text, ft.x, ft.y);
        ctx.restore();
    }
}

function drawVectorNPC(x, y, name) {
    ctx.fillStyle = '#0f172a';
    ctx.beginPath();
    ctx.roundRect(x - 14, y - 42, 28, 48, [10]);
    ctx.fill();

    ctx.fillStyle = '#fce7f3';
    ctx.beginPath();
    ctx.roundRect(x - 10, y - 30, 20, 16, [6]);
    ctx.fill();

    ctx.fillStyle = '#10b981';
    ctx.fillRect(x - 12, y - 38, 24, 10);

    ctx.fillStyle = 'rgba(15, 23, 42, 0.85)';
    ctx.beginPath();
    ctx.roundRect(x - 55, y - 62, 110, 20, [6]);
    ctx.fill();
    ctx.strokeStyle = 'rgba(16, 185, 129, 0.3)';
    ctx.stroke();

    ctx.fillStyle = '#ffffff';
    ctx.font = '600 12px Pretendard, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText(name, x, y - 48);
}

requestAnimationFrame(update);
</script>
</body>
</html>
"""

components.html(game_html, height=980)

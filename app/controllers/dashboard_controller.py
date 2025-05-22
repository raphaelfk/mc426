from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from app.models.route import Route
from app.models.user import User
from app import db

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
@login_required
def index():
    return render_template('dashboard/dashboard.html')

@dashboard_bp.route('/api/routes', methods=['GET'])
@login_required
def get_routes():
    routes = Route.query.filter_by(user_id=current_user.id, is_active=True).all()
    return jsonify([{
        'id': route.id,
        'start_point': route.start_point,
        'end_point': route.end_point
    } for route in routes])

@dashboard_bp.route('/api/routes', methods=['POST'])
@login_required
def create_route():
    data = request.get_json()
    route = Route(
        start_point=data['start_point'],
        end_point=data['end_point'],
        user_id=current_user.id
    )
    db.session.add(route)
    db.session.commit()
    return jsonify({
        'id': route.id,
        'start_point': route.start_point,
        'end_point': route.end_point
    })

@dashboard_bp.route('/api/routes/<int:route_id>', methods=['DELETE'])
@login_required
def delete_route(route_id):
    route = Route.query.get_or_404(route_id)
    if route.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    route.is_active = False
    db.session.commit()
    return jsonify({'message': 'Route deleted'})

@dashboard_bp.route('/api/matches', methods=['GET'])
@login_required
def get_matches():
    other_routes = Route.query.filter(
        Route.user_id != current_user.id,
        Route.is_active == True
    ).all()
    
    matches = []
    for route in other_routes:
        user = User.query.get(route.user_id)
        matches.append({
            'user_id': user.id,
            'username': user.username,
            'start_point': route.start_point,
            'end_point': route.end_point
        })
    
    return jsonify(matches) 